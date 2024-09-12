# https://chatgpt.com/c/5e331d27-bbba-4e2e-8413-ef946d1befe2

# Obtener todas las subcarpetas que coinciden con el formato "etiquetas_????"
$subcarpetas = Get-ChildItem -Directory -Filter "etiquetas_????"

# Verificar si hay subcarpetas que coinciden con el formato
if ($subcarpetas.Count -eq 0) {
    Write-Host "No se encontraron carpetas de etiquetas (formato 'etiquetas_????')."
    exit
}

# Mostrar las subcarpetas encontradas
Write-Host "Carpetas de etiquetas encontradas:"
$subcarpetas | ForEach-Object { Write-Host $_.Name }

# Solicitar al usuario que introduzca los últimos cuatro caracteres de una subcarpeta
$seleccion = Read-Host "Introduce los últimos cuatro caracteres de la carpeta de etiquetas a listar: "

# Buscar y mostrar la subcarpeta seleccionada
$subcarpetaSeleccionada = $subcarpetas | Where-Object { $_.Name.EndsWith($seleccion) }

if ($subcarpetaSeleccionada) {
    Write-Host "Has seleccionado la carpeta: $($subcarpetaSeleccionada.Name)"
    
    # Listar los archivos de la subcarpeta seleccionada
    $archivos = Get-ChildItem -Path $subcarpetaSeleccionada.FullName -File
    if ($archivos.Count -eq 0) {
        Write-Host "No se encontraron etiquetas en la carpeta seleccionada."
    } else {
        Write-Host "Etiquetas encontradas:"
        $archivos | ForEach-Object { Write-Host $_.Name }
    }
} else {
    Write-Host "No se encontró la carpeta 'etiquetas_$seleccion'."
}
