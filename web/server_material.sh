#!/bin/bash

# Perfil
source ~/miniconda3/etc/profile.d/conda.sh

conda activate zebra

cd /opt/iiot/codebar/web
python ./etiquetas_material_app.py

read -n 1 -s -r -p "Finalizado. Presione cualquier tecla para continuar..."
echo " "
