#!/bin/bash
source ~/miniconda3/etc/profile.d/conda.sh
echo "Genera etiqutas usando inventario_230623_v2.zpl. Se borraran la etiquetas anteriores en la carpeta 'out'"

rm ./out/*.zpl

conda activate zebra
read -n 1 -s -r -p "Copie en el clipboard la planilla a generar y presione cualquier tecla para continuar..."

python ./zpl_gen.py inventario_230623_v2.zpl -o ./out/

read -n 1 -s -r -p "Finalizado. Presione cualquier tecla para continuar..."
echo " "

