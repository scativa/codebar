# Changelog

Todas las fechas en formato ISO (YYYY-MM-DD).  
El proyecto sigue [Semantic Versioning](https://semver.org/) de forma aproximada.

---

## [2.1.0] — 2026-06-17

### Corregido
- `salvaguardia/zpl_gen.py`: Error de datos en generación de etiquetas de salvaguardia.
- `web/etiquetas_salvaguardia_app.py`: Error `UndefinedError: 'datos' is undefined` al acceder a `GET /`. Se agregó `datos={}` al render_template.

### Agregado
- `web/informe-bugs.md`: Registro de fallas conocidas y su resolución.

---

## [2.0.0] — 2025-06-25

### Agregado
- **Web app de salvaguardia** (`web/etiquetas_salvaguardia_app.py`): interfaz web para subir archivos ZPL e imprimir en impresora seleccionada, con selección de archivo individual o carpeta completa.
- **Web app de material** (`web/etiquetas_material_app.py`): generador visual de etiquetas con campos de formulario, preview mediante Labelary API, edición de JSON y ZPL inline, descarga de archivos, e impresión nativa Linux/Windows (win32print).
- Templates HTML separados por app (`templates_mat/`, `templates_salv/`).
- Servidores de inicio (`server_material.sh`, `server_salvaguardia.sh`).

---

## [1.5.0] — 2024-09-12

### Agregado
- Referencias a scripts de generación e impresión en README.

---

## [1.4.0] — 2024-08-13

### Agregado
- Opción `--json` en `zpl_gen.py` para generar archivo `.json` por cada etiqueta junto al `.zpl`.

---

## [1.3.0] — 2024-07-30

### Agregado
- Script `imprimir_menu.sh`: menú interactivo para seleccionar carpeta de etiquetas e imprimir todas o una en particular.
- Script `imprimir_etiquetas.sh`: impresión por lotes para Linux.
- Documentación de scripts en README.

---

## [1.2.0] — 2024-07-18

### Agregado
- Script `generar_etiquetas.sh` para Linux (Bash).
- Script `generar_etiquetas.ps1` para Windows (PowerShell).
- Script `generar_etiquetas.bat` para Windows (Explorador → llama al .ps1).
- `README.md` propio en `salvaguardia/`.

---

## [1.1.0] — 2024-07-01

### Cambiado
- Reorganización del proyecto: separación del flujo de inventario/salvaguardia en subdirectorio `salvaguardia/`.
- Rama `Inventario2024` fusionada a main.
- Actualización de templates ZPL para el inventario 2024.

---

## [1.0.0] — 2024-06-28

### Agregado
- Entorno de producción completo para inventario 2024.
- Template `inventario_230623_v2.zpl_t` con código QR (`^BQ`) para identificación por lote.
- Script `zpl_gen.py` con interfaz `argparse`: template, CSV/clipboard, directorio de salida.

---

## [0.5.0] — 2023-06-29

### Agregado
- Template `label_rectificado.zpl` con código de barras (`^BC`) para bandejas de rectificado.
- Script `shellcomand`: helpers para shell.

---

## [0.4.0] — 2023-06-28

### Agregado
- Modelo de etiqueta de inventario con código de barras.
- Separación de `inventario` como línea de trabajo independiente.

---

## [0.3.0] — 2023-06-22

### Agregado
- Librería `mod_zpl_template.py` con tres orígenes de datos: **CSV**, **JSON** y **portapapeles**.
- Conversión CSV → JSON → ZPL (`csv2label_inv_byjason.py`).

---

## [0.2.0] — 2023-06-15

### Agregado
- Nuevo esquema de trabajo: template `.zpl` + archivo `data.json`.
- Versión legacy marcada como deprecada.
- README.md con estructura y orden de archivos.

### Cambiado
- Reordenamiento de archivos en subdirectorios `csv/`, `json/`, `zpl/`.

---

## [0.1.0] — 2022-07-27

### Agregado
- Primer commit: generación básica de etiquetas ZPL desde tabla copiada al portapapeles.
- Impresión directa a impresora Zebra.

---

## Historial de commits (referencia)

Para el historial completo de cambios por commit, consultar:

```bash
git log --oneline --reverse
```
