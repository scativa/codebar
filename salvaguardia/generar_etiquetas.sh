#!/bin/bash
source ~/miniconda3/etc/profile.d/conda.sh

carpeta=./etiquetas/
zpl_template=inventario_230623_v2.zpl_t

echo "Genera etiqutas usando '$zpl_template'. Se borraran la etiquetas anteriores en la carpeta '$carpeta'"

if [ -d "$carpeta" ]; then
    echo "Eliminando archivos zpl de la carpeta '${carpeta}'"
    rm "${carpeta:?}"/*.zpl
else
    echo "Creando carpeta de salida '${carpeta}'"
    mkdir "${carpeta}"
fi

conda activate zebra
read -n 1 -s -r -p "Copie en el clipboard la planilla a generar y presione cualquier tecla para continuar..."

python ./zpl_gen.py "${zpl_template}" -o "${carpeta}"

read -n 1 -s -r -p "Finalizado. Presione cualquier tecla para continuar..."
echo " "

