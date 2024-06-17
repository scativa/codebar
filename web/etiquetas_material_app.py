from flask import Flask, render_template_string, request, send_file, redirect, flash
import os
import json
import base64
import subprocess
import requests
from datetime import datetime
import platform

if platform.system() == "Windows":
    import win32print
    import win32api

app = Flask(__name__, template_folder="templates_mat")
app.secret_key = "clave_secreta"

# -------------------------------
# Archivos base
# -------------------------------
ZPL_FILE = "template.zpl"
JSON_FILE = "listado.json"
OUTPUT_DIR = "zpl_guardados"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# -------------------------------
# HTML principal
# -------------------------------
HTML_BASE = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>🧾 Generador de Etiquetas Material</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body class="bg-dark text-light">
<div class="container mt-4">
    <h2 class="text-center mb-4">🧾 Generador de Etiquetas Material</h2>

    <div class="mb-3 text-end">
        <a href="/editor/json" class="btn btn-warning btn-sm">Editar JSON</a>
        <a href="/editor/zpl" class="btn btn-info btn-sm">Editar ZPL</a>
    </div>

    {% with messages = get_flashed_messages() %}
      {% if messages %}
        {% for msg in messages %}
          <div class="alert alert-info">{{ msg }}</div>
        {% endfor %}
      {% endif %}
    {% endwith %}

    <form method="POST" action="/">
        <div class="row">
            {% for key, label, opciones in campos %}
            <div class="col-md-4 mb-3">
                <label>{{ label }}</label>

                {% if opciones %}
                    <select name="{{ key }}" class="form-select" required>
                        <option value="">Seleccionar</option>
                        {% for opt in opciones %}
                            <option value="{{ opt }}" {% if valores.get(key) == opt %}selected{% endif %}>{{ opt }}</option>
                        {% endfor %}
                    </select>

                {% elif "FECHA" in key %}
                    <input type="date" name="{{ key }}" class="form-control" required
                           value="{{ valores.get(key, default_fecha) }}">

                {% else %}
                    <input type="text" name="{{ key }}" class="form-control" required
                           value="{{ valores.get(key, '') }}">
                {% endif %}
            </div>
            {% endfor %}
        </div>

        <div class="mb-3">
            <label>Impresora</label>
            <select name="printer" class="form-select" required>
                <option value="" selected>Seleccionar impresora</option>
                {% for p in impresoras %}
                    <option value="{{ p }}" {% if valores.get('printer') == p %}selected{% endif %}>{{ p }}</option>
                {% endfor %}
            </select>
        </div>

        <button type="submit" name="action" value="generate" class="btn btn-success">Generar vista previa</button>
        <button type="submit" name="action" value="print" class="btn btn-primary">🖨️ Imprimir</button>
    </form>

    {% if zpl %}
        <hr>
        <h5>ZPL generado:</h5>
        <pre class="bg-secondary p-3 rounded">{{ zpl }}</pre>
        <a href="/download" class="btn btn-warning">⬇️ Descargar .ZPL</a>

        {% if preview %}
            <h5 class="mt-3">Vista previa real (10x6 cm):</h5>
            <div class="text-center">
                <img src="data:image/png;base64,{{ preview }}" class="border rounded shadow" style="max-width:100%; height:auto;">
            </div>
        {% endif %}
    {% endif %}
</div>
</body>
</html>
"""

# -------------------------------
# EDITOR HTML
# -------------------------------
EDITOR_HTML = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>{{ titulo }}</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body class="bg-dark text-light">
<div class="container mt-4">

    <h3>{{ titulo }}</h3>
    <a href="/" class="btn btn-secondary btn-sm">⬅ Volver</a>

    {% with messages = get_flashed_messages() %}
      {% if messages %}
        {% for msg in messages %}
          <div class="alert alert-info mt-3">{{ msg }}</div>
        {% endfor %}
      {% endif %}
    {% endwith %}

    <form method="POST">
        <textarea name="contenido" rows="25" class="form-control bg-light">{{ contenido }}</textarea>
        <button class="btn btn-success mt-3" type="submit">Guardar</button>
    </form>

</div>
</body>
</html>
"""

# -------------------------------
# FUNCIONES
# -------------------------------
def obtener_impresoras():
    impresoras = []

    if platform.system() == "Linux":
        try:
            result = subprocess.run(['lpstat', '-a'], capture_output=True, text=True, check=True)
            for line in result.stdout.splitlines():
                nombre = line.split()[0]
                impresoras.append(nombre)
        except Exception as e:
            print("Error al obtener impresoras:", e)
    else:
        impresoras = [p[2] for p in win32print.EnumPrinters(2)]

    return impresoras


def imprimir_archivo_zpl(archivo, impresora):
    try:
        if platform.system() == "Linux":
            result = subprocess.run(['lpstat', '-p', impresora], capture_output=True, text=True)

            if "disabled" in result.stdout or "inactiva" in result.stdout.lower():
                subprocess.run(['sudo', 'cupsenable', impresora])
                subprocess.run(['sudo', 'cupsaccept', impresora])

            subprocess.run(["lp", "-d", impresora, "-o", "raw", archivo], check=True)

        else:
            win32api.ShellExecute(0, "printto", archivo, f'"{impresora}"', ".", 0)

        return True

    except Exception as e:
        print("Error imprimiendo:", e)
        return False


def leer_plantilla():
    with open(ZPL_FILE, "r", encoding="latin-1") as f:
        return f.read()


def leer_json():
    with open(JSON_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def render_zpl_to_image(zpl_data):
    url = "https://api.labelary.com/v1/printers/8dpmm/labels/10x6/0/"
    headers = {"Accept": "image/png"}
    r = requests.post(url, headers=headers, data=zpl_data.encode("latin-1"))
    return r.content


def generate_zpl(template, values):
    for k, v in values.items():
        template = template.replace(f"{{{k}}}", v)
    return template


# -------------------------------
# RUTA PRINCIPAL
# -------------------------------
@app.route("/", methods=["GET", "POST"])
def index():
    template = leer_plantilla()
    data = leer_json()
    impresoras = obtener_impresoras()
    default_fecha = datetime.now().strftime("%Y-%m-%d")

    campos = [
        ("RESP", "Responsable", data["Campos"].get("RESP", [])),
        ("ESTADO", "Estado", data["Campos"].get("ESTADO", [])),
        ("FECHA", "Fecha", []),
        ("MAT", "Material", data["Campos"].get("MAT", [])),
        ("ID", "Identificación", [])
    ]

    generated_zpl = None
    generated_preview = None

    if request.method == "POST":
        values = {}

        for key, _, _ in campos:
            val = request.form.get(key, "")
            if "FECHA" in key and val:
                val = datetime.strptime(val, "%Y-%m-%d").strftime("%d/%m/%Y")
            values[key] = val

        generated_zpl = generate_zpl(template, values)

        archivo_path = os.path.join(OUTPUT_DIR, "a_imprimir.zpl")
        with open(archivo_path, "w", encoding="latin-1") as f:
            f.write(generated_zpl)

        try:
            img = render_zpl_to_image(generated_zpl)
            generated_preview = base64.b64encode(img).decode("utf-8")
        except:
            pass

        if request.form["action"] == "print":
            impresora = request.form.get("printer", "")
            if impresora and imprimir_archivo_zpl(archivo_path, impresora):
                flash(f"Imprimiendo en: {impresora}")
            else:
                flash("Error al imprimir")

    return render_template_string(
        HTML_BASE,
        campos=campos,
        impresoras=impresoras,
        zpl=generated_zpl,
        preview=generated_preview,
        valores=request.form,
        default_fecha=default_fecha
    )


# ------------------------------- EDITOR JSON -------------------------------
@app.route("/editor/json", methods=["GET", "POST"])
def editor_json():
    if request.method == "POST":
        contenido = request.form["contenido"]
        try:
            json.loads(contenido)
            with open(JSON_FILE, "w", encoding="utf-8") as f:
                f.write(contenido)
            flash("JSON guardado correctamente.")
        except Exception as e:
            flash(f"Error: {e}")

        return redirect("/editor/json")

    with open(JSON_FILE, "r", encoding="utf-8") as f:
        contenido = f.read()

    return render_template_string(EDITOR_HTML, titulo="Editor JSON", contenido=contenido)


# ------------------------------- EDITOR ZPL -------------------------------
@app.route("/editor/zpl", methods=["GET", "POST"])
def editor_zpl():
    if request.method == "POST":
        contenido = request.form["contenido"]
        with open(ZPL_FILE, "w", encoding="latin-1") as f:
            f.write(contenido)
        flash("ZPL guardado correctamente.")
        return redirect("/editor/zpl")

    with open(ZPL_FILE, "r", encoding="latin-1") as f:
        contenido = f.read()

    return render_template_string(EDITOR_HTML, titulo="Editor ZPL", contenido=contenido)


# ------------------------------- DESCARGAR -------------------------------
@app.route("/download")
def download():
    archivos = sorted(os.listdir(OUTPUT_DIR))
    if not archivos:
        return "No hay archivos."

    ultima = os.path.join(OUTPUT_DIR, archivos[-1])
    return send_file(ultima, as_attachment=True)


# ------------------------------- RUN -------------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8081, debug=True)