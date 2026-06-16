from flask import Flask, render_template, request, redirect, flash
import os, sys
import subprocess

app = Flask(__name__)
app.secret_key = 'clave_secreta'

# Carpeta base donde se guardan las etiquetas
BASE_ETIQUETAS_DIR = os.path.abspath("etiquetas")


# Función para obtener las impresoras disponibles
def obtener_impresoras():
    result = subprocess.run(['lpstat', '-p'], capture_output=True, text=True)
    print(result)

    # Lista de impresoras disponibles
    impresoras = []
    for line in result.stdout.splitlines():
        if "impresora" in line:
            printer_name = line.split(' ')[2].strip()  # Eliminar espacios invisibles
            impresoras.append(printer_name)
            print(f"Impresora detectada: {printer_name}")  # Imprime para debug
        elif "printer" in line:
            printer_name = line.split(' ')[1].strip()  # Eliminar espacios invisibles
            impresoras.append(printer_name)
            print(f"Impresora detectada: {printer_name}")  # Imprime para debug

    print(f"Impresoras disponibles: {impresoras}")  # Verifica que solo zebra-raw esté en la lista
    return impresoras

def imprimir_archivo_zpl(archivo, impresora):
    try:
        subprocess.run(
            f'lp -d {impresora} <<< "$(cat \"{archivo}\")"',
            shell=True,
            check=True,
            executable='/bin/bash'
        )
    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"Error al imprimir archivo: {archivo} — {str(e)}")

# Imprimir todos los .zpl de una carpeta
def imprimir_carpeta_zpl(carpeta, impresora):
    if not os.path.isdir(carpeta):
        raise Exception(f"La carpeta no existe: {carpeta}")
    archivos = sorted([f for f in os.listdir(carpeta) if f.lower().endswith('.zpl')])
    if not archivos:
        raise Exception("No se encontraron archivos .zpl en la carpeta.")
    for archivo in archivos:
        ruta = os.path.join(carpeta, archivo)
        imprimir_archivo_zpl(ruta, impresora)

# Página principal (impresión)
@app.route('/')
def index():
    impresoras = obtener_impresoras()  # Obtiene las impresoras filtradas
    # TODO: el template index.html tiene links a /editor_zpl y /editor_json
    # que no están implementados en esta app. Revisar con el desarrollador
    # si deben agregarse o sacarse los links del template.
    return render_template('index.html', impresoras=impresoras, datos={})

# Enviar etiquetas a la impresora
@app.route('/imprimir', methods=['POST'])
def imprimir():
    tipo = request.form.get('tipo')
    impresora = request.form.get('printer')
    carpeta = request.form.get('carpeta', '').strip()
    archivo = request.form.get('archivo', '').strip()

    try:
        ruta_carpeta = os.path.join(BASE_ETIQUETAS_DIR, carpeta)

        if tipo == 'archivo':
            ruta = os.path.join(ruta_carpeta, archivo)
            if not ruta.lower().endswith('.zpl'):
                ruta += '.zpl'
            imprimir_archivo_zpl(ruta, impresora)
            flash(f"Archivo '{archivo}' enviado a la impresora.")
        elif tipo == 'carpeta':
            imprimir_carpeta_zpl(ruta_carpeta, impresora)
            flash("Todos los archivos .zpl de la carpeta fueron enviados.")
        else:
            flash("Tipo de impresión no válido.")
    except Exception as e:
        flash(f"Error: {str(e)}")

    return redirect('/')

# Página para subir archivos
@app.route('/subir', methods=['GET', 'POST'])
def subir():
    if request.method == 'POST':
        carpeta = request.form.get('carpeta', '').strip()
        archivos = request.files.getlist('zplfile[]')

        if not carpeta or not archivos or all(a.filename == '' for a in archivos):
            flash("Debés completar todos los campos y seleccionar al menos un archivo.")
            return redirect('/subir')

        destino = os.path.join(BASE_ETIQUETAS_DIR, carpeta)
        os.makedirs(destino, exist_ok=True)

        cantidad_subidos = 0
        for archivo in archivos:
            if archivo.filename.lower().endswith('.zpl'):
                ruta_guardado = os.path.join(destino, archivo.filename)
                archivo.save(ruta_guardado)
                cantidad_subidos += 1

        if cantidad_subidos:
            flash(f"{cantidad_subidos} archivos .zpl subidos a la carpeta '{carpeta}'.")
        else:
            flash("No se subió ningún archivo válido (.zpl).")

        return redirect('/subir')

    return render_template('subir.html')


# Iniciar servidor
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(f"Uso: python {sys.argv[0]} <puerto>")
        exit(1)
    else:
        port = sys.argv[1]
        print(f"Escuchando en puerto {port}")
        os.makedirs(BASE_ETIQUETAS_DIR, exist_ok=True)
        app.run(debug=True, port=port, host='0.0.0.0')