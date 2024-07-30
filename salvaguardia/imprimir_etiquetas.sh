#!/bin/bash

# Verificar si se ha pasado un parámetro
if [ $# -eq 0 ]; then
    echo "No se ha proporcionado ninguna carpeta como parámetro. Por defecto se utilizará la carpeta './etiquetas/'"
    carpeta=./etiquetas/
else
    # Obtener el nombre de la carpeta del primer parámetro
    carpeta="$1"
fi

# Verificar si la carpeta existe
if [ -d "$carpeta" ]; then
    # echo "La carpeta seleccionada es: $carpeta"
    echo " "
else
    echo "La carpeta '$carpeta' no existe."
    exit 1
fi

# Preguntar al usuario si desea imprimir todos los archivos .zpl o uno en particular
echo "¿Desea imprimir todas las etiquetas o una en particular?"
echo "1) Todas"
echo "2) Una en particular"
echo "Presiona ESC para cancelar."
read -n 1 -s opcion

# Función para capturar la tecla presionada
function press_key() {
    read -rsn1 input
    if [[ $input == $'\e' ]]; then
        echo -e "\nOperación cancelada por el usuario."
        exit 0
    fi
}

case $opcion in
    1)
        # Imprimir todos los archivos .zpl en la carpeta
        echo "Impresión de todas las etiquetas de la carpeta $PWD/${carpeta}"
        for file in "${carpeta}"/*.zpl; do
            lp -d zebra-raw <<< "$(cat "$file")"
        done
        ;;
    2)
        # Mostrar todos los archivos .zpl en la carpeta
        echo "Etiquetas disponibles en la carpeta '${carpeta}':"
        archivos=("${carpeta}"/*.zpl)
        for archivo in "${archivos[@]}"; do
            echo "$(basename "$archivo" .zpl)"
        done

        # Pedir al usuario el nombre del archivo .zpl (sin la extensión)
        echo "Ingrese el nombre de la etiqueta o presione ESC para cancelar: "
        press_key  # Llamar a la función para permitir cancelar con ESC

        read -p "" nombre_archivo

        # Verificar si se presionó ESC
        if [[ $nombre_archivo == $'\e' ]]; then
            echo "Operación cancelada por el usuario."
            exit 0
        fi

        archivo_seleccionado="${carpeta}/${nombre_archivo}.zpl"

        # Verificar si el archivo existe y luego imprimirlo
        if [ -f "$archivo_seleccionado" ]; then
            echo "Imprimiendo la etiqueta: $archivo_seleccionado"
            lp -d zebra-raw <<< "$(cat "$archivo_seleccionado")"
        else
            echo "El archivo '$archivo_seleccionado' no existe."
            exit 1
        fi
        ;;
    *)
        echo "Opción no válida. Saliendo..."
        exit 1
        ;;
esac

read -n 1 -s -r -p "Presione cualquier tecla para finalizar"
echo " "
