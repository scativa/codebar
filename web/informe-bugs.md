# Informe de Fallas — Web Salvaguardia

## Falla 1: `UndefinedError: 'datos' is undefined`

### Síntoma
Error 500 al acceder a `GET /` en `etiquetas_salvaguardia_app.py`.

```
jinja2.exceptions.UndefinedError: 'datos' is undefined
  File "etiquetas_salvaguardia_app.py", line 58, in index
    return render_template('index.html', impresoras=impresoras)
  File "templates/index.html", line 41, in top-level template code
    {% if datos.responsables %}
```

### Causa
La ruta `GET /` llamaba a `render_template('index.html', impresoras=impresoras)` sin pasar la variable `datos` que el template espera para los combos de Responsable y Estado.

### Solución aplicada
```python
# Antes
return render_template('index.html', impresoras=impresoras)

# Después
return render_template('index.html', impresoras=impresoras, datos={})
```
Con `datos={}` los `{% if datos.responsables %}` evalúan a `False` y los selects se renderizan sin opciones, evitando el crash.

**Archivo modificado:** `web/etiquetas_salvaguardia_app.py`

---

## Falla 2: Rutas de editor faltantes (por revisar)

### Síntoma
El template `templates/index.html` tiene links a `/editor_zpl` y `/editor_json`, pero esas rutas no existen en `etiquetas_salvaguardia_app.py`. Clickearlas da 404.

### Causa
El template se comparte entre `etiquetas_material_app.py` (que sí tiene los editores) y `etiquetas_salvaguardia_app.py` (que no). Los links quedaron visiblemente activos en la app de salvaguardia sin las rutas correspondientes.

### Estado
⚠️ **Pendiente de revisión con el desarrollador.** Decidir si:
- Agregar las rutas de editor a `etiquetas_salvaguardia_app.py`
- O sacar los links del template `index.html`

**Archivos con TODOs:**
- `web/etiquetas_salvaguardia_app.py` — comentario en ruta `GET /`
- `web/templates/index.html` — comentario antes de los links

---

## Revisión general

Se inspeccionaron todas las llamadas a `render_template` y `render_template_string` en `web/`:

| App | Ruta | Estado |
|-----|------|--------|
| `etiquetas_salvaguardia_app.py` — `GET /` | ✅ Corregido |
| `etiquetas_salvaguardia_app.py` — `GET /subir` | ✅ Sin errores |
| `etiquetas_material_app.py` — `GET /` | ✅ Sin errores |
| `etiquetas_material_app.py` — `GET /editor/json` | ✅ Sin errores |
| `etiquetas_material_app.py` — `GET /editor/zpl` | ✅ Sin errores |

No se encontraron otras variables faltantes en las llamadas a templates.
