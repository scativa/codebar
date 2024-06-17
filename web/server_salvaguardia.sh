#!/bin/bash

# Nombre de la carpeta
folderName="etiquetas"

# Perfil
source ~/miniconda3/etc/profile.d/conda.sh
carpeta=./$folderName/

conda activate zebra

cd /opt/iiot/codebar/web
python ./etiquetas_salvaguardia_app.py 8080

read -n 1 -s -r -p "Finalizado. Presione cualquier tecla para continuar..."
echo " "

