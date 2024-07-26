# Obtener todas las subcarpetas que coinciden con el formato "etiquetas_????"
$subcarpetas = Get-ChildItem -Directory -Filter "etiquetas_????"

# Verificar si hay subcarpetas que coinciden con el formato
if ($subcarpetas.Count -eq 0) {
    Write-Host "No se encontraron subcarpetas con el formato 'etiquetas_????'."
    exit
}

# Mostrar las subcarpetas encontradas
Write-Host "Subcarpetas encontradas:"
$subcarpetas | ForEach-Object { Write-Host $_.Name }

# Solicitar al usuario que introduzca los últimos cuatro caracteres de una subcarpeta
$seleccion = Read-Host "Introduce los últimos cuatro caracteres de una subcarpeta"

# Buscar y mostrar la subcarpeta seleccionada
$subcarpetaSeleccionada = $subcarpetas | Where-Object { $_.Name.EndsWith($seleccion) }

if ($subcarpetaSeleccionada) {
    Write-Host "Has seleccionado la subcarpeta: $($subcarpetaSeleccionada.Name)"
    
    # Listar los archivos de la subcarpeta seleccionada
    $archivos = Get-ChildItem -Path $subcarpetaSeleccionada.FullName -File
    if ($archivos.Count -eq 0) {
        Write-Host "No se encontraron archivos en la subcarpeta seleccionada."
    } else {
        Write-Host "Archivos en la subcarpeta seleccionada:"
        $archivos | ForEach-Object { Write-Host $_.Name }
    }
} else {
    Write-Host "No se encontró una subcarpeta que termine con '$seleccion'."
}
