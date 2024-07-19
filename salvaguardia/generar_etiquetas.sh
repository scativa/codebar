#!/bin/bash
# https://chatgpt.com/c/5e331d27-bbba-4e2e-8413-ef946d1befe2

# Generar un número aleatorio de seis dígitos
randomNumber=$(shuf -i 1000-9999 -n 1)

# Prefijo de la carpeta
prefix="etiquetas_"

# Nombre de la carpeta
folderName="${prefix}${randomNumber}"

# Perfil
source ~/miniconda3/etc/profile.d/conda.sh

carpeta=./$folderName/
zpl_template=inventario_230623_v2.zpl_t

echo "Genera etiqutas usando '$zpl_template'"

if [ -d "$carpeta" ]; then
    read -n 1 -s -r -p "Se borraran la etiquetas anteriores de la carpeta '$carpeta'. Presione Enter para continuar..."
    echo "Eliminando archivos zpl de la carpeta '${carpeta}'"
    rm "${carpeta:?}"/*.zpl
else
    echo "Creando carpeta de salida '${carpeta}'"
    mkdir -p "${carpeta}" > /dev/null 2>&1
    # mkdir -p "$folderPath" > /dev/null 2>&1
fi

conda activate zebra
read -n 1 -s -r -p "Copie en el clipboard la planilla a generar y presione cualquier tecla para continuar..."

python ./zpl_gen.py "${zpl_template}" -o "${carpeta}"

read -n 1 -s -r -p "Finalizado. Presione cualquier tecla para continuar..."
echo " "

