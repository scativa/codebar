#!/bin/bash

# Verificar si se ha pasado un parámetro
if [ $# -eq 0 ]; then
    echo "No se ha proporcionado ninguna carpeta como parámetro. Por defecto se utilzará la carpeta "${carpeta}""
	carpeta=./etiquetas/
else
	# Obtener el nombre de la carpeta del primer parámetro
	carpeta="$1"
fi


# Verificar si la carpeta existe
if [ -d "$carpeta" ]; then
    echo "La carpeta seleccionada es: $carpeta"
else
    echo "La carpeta '$carpeta' no existe."
    exit 1
fi

echo "Impresión de todos los archivos de la carpeta $PWD/"${carpeta}""
for file in "${carpeta}"/*.zpl; do lp -d zebra-raw <<< "$(cat "$file")"; done
read -n 1 -s -r -p "Presione cualquier tecla para finalizar"
echo " "
