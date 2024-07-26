#!/bin/bash

# Obtener todas las subcarpetas que coinciden con el formato "etiquetas_????"
subcarpetas=($(find . -type d -name "etiquetas_????"))

# Verificar si hay subcarpetas que coinciden con el formato
if [ ${#subcarpetas[@]} -eq 0 ]; then
    echo "No se encontraron subcarpetas con el formato 'etiquetas_????'."
    exit 1
fi

# Mostrar las subcarpetas encontradas
echo "Subcarpetas encontradas:"
for subcarpeta in "${subcarpetas[@]}"; do
    echo "$(basename "$subcarpeta")"
done

# Solicitar al usuario que introduzca los últimos cuatro caracteres de una subcarpeta
read -p "Introduce los últimos cuatro caracteres de una subcarpeta: " seleccion

# Buscar y mostrar la subcarpeta seleccionada
subcarpetaSeleccionada=""
for subcarpeta in "${subcarpetas[@]}"; do
    if [[ "$(basename "$subcarpeta")" == *"$seleccion" ]]; then
        subcarpetaSeleccionada="$subcarpeta"
        break
    fi
done

if [ -n "$subcarpetaSeleccionada" ]; then
    echo "Has seleccionado la subcarpeta: $(basename "$subcarpetaSeleccionada")"
    
    # Listar los archivos de la subcarpeta seleccionada
    archivos=($(find "$subcarpetaSeleccionada" -maxdepth 1 -type f))
    if [ ${#archivos[@]} -eq 0 ]; then
        echo "No se encontraron archivos en la subcarpeta seleccionada."
    else
        echo "Archivos en la subcarpeta seleccionada:"
        for archivo in "${archivos[@]}"; do
            echo "$(basename "$archivo")"
        done
    fi

    # Llamar al script "imprimir_etiquetas.sh" pasando la carpeta seleccionada como parámetro
    ./imprimir_etiquetas.sh "$subcarpetaSeleccionada"
else
    echo "No se encontró una subcarpeta que termine con '$seleccion'."
fi
