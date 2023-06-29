#!/bin/bash
echo "Impresión de todos los archivos de la carpeta $PWD"
cd ../out
for file in *.zpl; do lp -d zebra-raw <<< "$(cat "$file")"; done
cd ..
read -n 1 -s -r -p "Presione cualquier tecla para finalizar"
echo " "

