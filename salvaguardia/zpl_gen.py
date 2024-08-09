################################
## Generador ZPL 
##
## Genera archivos de etiquetas zpl partiendo de información en formato CSV
## que puede ser leido de un archivo en disco o de clipboard. 
##
## Estructura CSV
## La primer fila debe contener los tags para reemplazar en el tamplate. Para
## en las filas siguiente, cada columna representan el valor del tag a ser 
## reemplazado en el template .zlp_t
## 
##
## ARGS:
## - zpl_template: Archivo a usarse de modelo que se completa con
##   los valores de los tags
## 
## --csv: Archivo CSV de entrada. De ser NULL se toma lo existente
##        en el clipboard
##
## --outdir: Carpeta de salida donde se graban los archivos de etiqueta generados
################################

import mod_zpl_template as mzpl
import json
import os
import argparse
import pyperclip
import io

# def save_zpl(etiqueta, id_field, out_dir):
#     fn = etiqueta[1][id_field]
#     full_path = os.path.join(out_dir, f'{fn}.zpl')
#     with open(full_path, 'w') as archivo:
#         lineas = etiqueta[2].splitlines()
#         for linea in lineas:
#             archivo.write(linea + '\n')    
#         print(f'{fn}.zpl')

def save_zpl(etiqueta, fn, out_dir):
    # fn = etiqueta[1][id_field]
    full_path = os.path.join(out_dir, f'{fn}.zpl')
    with open(full_path, 'w') as archivo:
        lineas = etiqueta.splitlines()
        for linea in lineas:
            archivo.write(linea + '\n')    

def save_json(data, fn, out_dir):
    # Escribir los datos en el archivo JSON
    # Fuente ../json/mod_csv2json.py
    full_path = os.path.join(out_dir, f'{fn}.json')
    with open(full_path, 'w') as file:
        json.dump(data, file, indent=4)

parser = argparse.ArgumentParser()
# parser.add_argument('files', nargs='*', help='nombres de archivo (opcionales)')
parser.add_argument('zpl_template', help='archivo ZPL con tags a ser usado como template')
# parser.add_argument('-v', '--clipboard', action='store_true', help='tomar nombres de archivo del portapapeles')
parser.add_argument('--csv', required=False, help='archivo de entrada csv con los datos de las etiquetas. Vacío para tomar el clipboard')
parser.add_argument('-o', '--outdir', default='.', help='carpeta de salida donde se graban los archivos de etiqueta generados')
parser.add_argument('--json', action='store_true', help="Indica si se debe generar archivos JSON")
args = parser.parse_args()

zpl_template = args.zpl_template
out_dir = args.outdir
csv_file_name = args.csv
gen_json = args.json
# clipboard = args.clipboard

# file_names = args.files
print(f'Modelo zpl: {zpl_template}')
print(f'Carpeta de salida: {out_dir}')
print(f'Datos de entrada: {"Clipboard" if csv_file_name is None else csv_file_name}')

if csv_file_name is None:
    # Pegado de CSV de porta papeles
    paste = pyperclip.paste()
    csv_file = io.StringIO(paste)
    data_dict = mzpl.csv_to_dict(csv_file, delimiter='\t')
else:
    # Lectura de CSV directo a dict
    with open(csv_file_name, 'r') as csv_file:
        data_dict = mzpl.csv_to_dict(csv_file, delimiter=',')

etiquetas = mzpl.generate_zpl_content(zpl_template, data_dict)

print(f'Etiquetas encontradas: {len(etiquetas)}')
for etiqueta in etiquetas:
    
    fn = etiqueta[1]['_idlote']
    save_zpl(etiqueta[2],fn,out_dir)
    msg_out = f'{fn}.zpl'
    if gen_json:
        save_json(etiqueta[1],fn,out_dir)
        msg_out = f'{msg_out} + {fn}.json'
    print(msg_out)

# for row in data_dict:
#     csvjson.save_json(row,'_idlote',out_dir)