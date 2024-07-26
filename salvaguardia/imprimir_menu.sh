#!/bin/bash

# Obtener todas las subcarpetas que coinciden con el formato "etiquetas_????"
subcarpetas=($(find . -type d -name "etiquetas_????"))

# Verificar si hay subcarpetas que coinciden con el formato
if [ ${#subcarpetas[@]} -eq 0 ]; then
    echo "No se encontraron carpetas de etiquetas (formato 'etiquetas_????')."
    exit 1
fi

# Mostrar las subcarpetas encontradas
echo "Carpetas de etiquetas encontradas:"
for subcarpeta in "${subcarpetas[@]}"; do
    echo "$(basename "$subcarpeta")"
done

# Solicitar al usuario que introduzca los últimos cuatro caracteres de una subcarpeta
read -p "Introduce los últimos cuatro caracteres de la carpeta de etiquetas a imprimir: " seleccion

# Buscar y mostrar la subcarpeta seleccionada
subcarpetaSeleccionada=""
for subcarpeta in "${subcarpetas[@]}"; do
    if [[ "$(basename "$subcarpeta")" == *"$seleccion" ]]; then
        subcarpetaSeleccionada="$subcarpeta"
        break
    fi
done

if [ -n "$subcarpetaSeleccionada" ]; then
    echo "Has seleccionado la carpeta: $(basename "$subcarpetaSeleccionada")"
    
    # Listar los archivos de la subcarpeta seleccionada
    archivos=($(find "$subcarpetaSeleccionada" -maxdepth 1 -type f))
    if [ ${#archivos[@]} -eq 0 ]; then
        echo "No se encontraron etiquetas en la carpeta seleccionada."
    else
        echo "Etiquetas a imprimir:"
        for archivo in "${archivos[@]}"; do
            echo "$(basename "$archivo")"
        done

        while true; do
            echo "Presiona ENTER para imprimir o ESC para cancelar."
            read -rsn1 input
            if [[ $input == $'\e' ]]; then
                echo "Impresión cancelada por el usuario. Presione cualquier tecla para finalizar"
                read -rsn1 input
                exit 0
            elif [[ -z $input ]]; then
                echo "Imprimiendo: $carpeta"

                # Llamar al script "imprimir_etiquetas.sh" pasando la carpeta seleccionada como parámetro
                ./imprimir_etiquetas.sh "$subcarpetaSeleccionada"

                exit 0
            fi
        done
    fi

else
    echo "No se encontró la carpeta 'etiquetas_$seleccion'."
fi
