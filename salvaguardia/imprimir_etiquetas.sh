#!/bin/bash
carpeta=./etiquetas/

echo "Impresión de todos los archivos de la carpeta $PWD/"${carpeta}""
for file in "${carpeta}"/*.zpl; do lp -d zebra-raw <<< "$(cat "$file")"; done
read -n 1 -s -r -p "Presione cualquier tecla para finalizar"
echo " "
