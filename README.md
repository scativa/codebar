# codebar

Generación e impresión de etiquetas ZPL para impresoras térmicas **Zebra GC420t**. El sistema reemplaza marcadores en plantillas ZPL con datos provenientes de archivos CSV, JSON o del portapapeles, produciendo etiquetas listas para imprimir.

Desarrollado para la **Planta Piloto de Combustibles Avanzados (PPCA)** de la Comisión Nacional de Energía Atómica (CNEA).

---

## Requisitos

- **Python** 3.10.4
- **pip** `pyperclip` — acceso al portapapeles del sistema
- **Conda** (recomendado) para aislar el entorno

### Linux

```bash
sudo apt install xclip
```

### Windows

No requiere dependencias adicionales de sistema. La dependencia `pyperclip` funciona con el portapapeles nativo de Windows.

---

## Configuración del entorno

```bash
conda create -n zebra python=3.10.4
conda activate zebra
python -m pip install -r requirements.txt
```

---

## Estructura del proyecto

```
codebar/
├── mod_zpl_template.py      # Librería principal: procesamiento de templates ZPL
├── json2label.py             # Genera ZPL desde archivo JSON + template
├── csv2label_inv_byjason.py  # Convierte CSV → JSON → ZPL
├── pastetable.py             # Lee CSV del portapapeles
├── requirements.txt          # Dependencias del proyecto
├── .gitignore
├── README.md
├── CHANGELOG.md
│
├── csv/                      # Ejemplos de manejo de CSV
│   └── readtable.py
│
├── json/                     # Ejemplos de manejo de JSON
│   ├── datos.json
│   ├── inventario.json
│   ├── tabla.json
│   ├── json_recursive.py
│   ├── str2json.py
│   └── mod_csv2json.py
│
├── zpl/                      # Ejemplos de templates y utilidades ZPL
│   ├── label_rectificado.zpl
│   └── parse_zpl_line.py
│
├── from_csv/                 # (vacío — directorio de trabajo)
├── out/                      # Salida de etiquetas generadas
│
├── salvaguardia/             # Versión específica para controles anuales de salvaguardia
│   ├── zpl_gen.py            # Generador ZPL de producción (CLI con argparse)
│   ├── mod_zpl_template.py   # Copia de la librería base
│   ├── inventario_230623_v2.zpl_t  # Template ZPL para inventario
│   ├── csv/                  # Datos de inventario
│   ├── codigos/              # Generación de códigos de inventario
│   ├── generar_etiquetas.sh  # Script de generación para Linux
│   ├── generar_etiquetas.ps1 # Script de generación para Windows PowerShell
│   ├── generar_etiquetas.bat # Script de generación para Explorador de Windows
│   ├── imprimir_etiquetas.sh # Script de impresión
│   ├── imprimir_menu.sh      # Menú interactivo de impresión
│   └── listar_etiquetas.ps1
│
├── material_lab/             # Configuración para etiquetas de material de laboratorio
│   ├── listado.json          # Datos de responsables, materiales y estados
│   └── material_template.zpl # Template específico para material
│
├── web/                      # Aplicaciones web Flask
│   ├── etiquetas_salvaguardia_app.py  # Web app: impresión de salvaguardia
│   ├── etiquetas_material_app.py      # Web app: generación de etiquetas de material
│   ├── template.zpl          # Template ZPL para la web
│   ├── listado.json          # Datos comunes (responsable, estado, material)
│   ├── templates_mat/        # Templates HTML para app de material
│   ├── templates_salv/       # Templates HTML para app de salvaguardia
│   ├── server_material.sh    # Script de inicio servidor material
│   ├── server_salvaguardia.sh # Script de inicio servidor salvaguardia
│   └── informe-bugs.md       # Registro de fallas corregidas
│
└── openspec/                 # Configuración SDD (Spec-Driven Development)
    └── config.yaml
```

---

## Funcionalidad

### 1. Procesamiento de templates ZPL

La librería `mod_zpl_template.py` provee funciones para:

- **`csv_to_dict(csv_file, delimiter)`** — Lee un archivo CSV y lo convierte en lista de diccionarios.
- **`csv_to_jsonfile(csv_file, json_file, delimiter)`** — Convierte CSV a JSON intermedio.
- **`generate_zpl_content(modelo_zpl_path, data_list)`** — Toma un template ZPL y una lista de datos, reemplaza los marcadores (`{marca}`) y devuelve el ZPL generado.
- **`print_zpl_content(modelo_zpl_path, data_list)`** — Función equivalente que imprime por pantalla.

### 2. Generación de etiquetas por línea de comandos

**Desde el portapapeles** (copiar datos con formato CSV/TSV):

```bash
python salvaguardia/zpl_gen.py modelo.zpl -o ./out/
```

**Desde un archivo CSV**:

```bash
python salvaguardia/zpl_gen.py modelo.zpl -o ./out/ --csv ./datos.csv
```

**Desde un archivo JSON**:

```bash
python json2label.py
```

### 3. Generación de etiquetas con JSON + JSON opcional

```bash
python salvaguardia/zpl_gen.py modelo.zpl -o ./out/ --csv ./datos.csv --json
```

Esto genera un archivo `.json` por cada etiqueta además del `.zpl`.

### 4. Impresión de etiquetas

**Impresora Zebra (Linux — cola `zebra-raw`):**

```bash
# Una etiqueta
lp -d zebra-raw label.zpl

# Todas las etiquetas de la carpeta
for file in *.zpl; do lp -d zebra-raw <<< "$(cat "$file")"; done
```

### 5. Web Apps (Flask)

Dos aplicaciones web independientes:

| App | Puerto | Función |
|-----|--------|---------|
| `etiquetas_material_app.py` | `8081` | Generación visual de etiquetas de material con preview Labelary y edición de JSON/ZPL |
| `etiquetas_salvaguardia_app.py` | configurable | Subida e impresión de etiquetas ZPL, selección de impresora |

```bash
# Iniciar app de material
bash web/server_material.sh

# Iniciar app de salvaguardia
bash web/server_salvaguardia.sh
```

### 6. Scripts de producción (Salvaguardia)

El subdirectorio `salvaguardia/` contiene scripts listos para el flujo anual de inventario:

- **Linux:** `generar_etiquetas.sh` → copiar datos al portapapeles, ejecuta `zpl_gen.py`, guarda en carpeta `etiquetas_XXXX`.
- **Windows:** `generar_etiquetas.ps1` (PowerShell) o `generar_etiquetas.bat` (Explorador).
- **Impresión:** `imprimir_menu.sh` permite seleccionar una carpeta de etiquetas generadas e imprimir todas o una en particular.

---

## Formato de datos

### CSV

La primera fila debe contener los nombres de los marcadores (tags) a reemplazar en el template ZPL. Cada fila subsiguiente es una etiqueta.

```csv
_idlote,_pbruto,_ptara,_pneto,_pelem,_pisot,_citem,_codmat,_enriq,_elem,_u
L24-001,4500,500,4000,3800,3500,24 items,MOX,4.5,Pu,gr
```

### Template ZPL

Los marcadores se escriben entre llaves `{}` en el archivo `.zpl` o `.zpl_t`:

```
^FO55,170^BQ,2,6^FDQA,_idlote^FS
^FO760,60,1^AN,30^FD_pbruto^FS
```

---

## Utilidades

- **[Labelary](http://labelary.com/viewer.html)** — Previsualiza etiquetas ZPL online.
- **[jszpl](https://www.npmjs.com/package/jszpl)** — Librería JavaScript para generar ZPL.
- **[Zebra - pypi](https://pypi.org/project/zebra/)** — Paquete Python para comunicación con impresoras Zebra.
- **[PythonPcl](https://github.com/mchobby/PythonPcl)** — Librería Python para impresión raw en Zebra.

---

## Documentación adicional

- [Versión Google Docs](https://docs.google.com/document/d/1KEMTndB9a6GAG9w_y4i5BaqnAcqN8ZQys83Q_9N4GOU/edit?usp=sharing)
- [Configuración proxy para CNEA](https://docs.google.com/document/d/1PBPeE-3_t7xeguKVyJ43NtW8PBHgLuLB9SqO0_dvmN0/edit#heading=h.bbutr3mgg8o5)
