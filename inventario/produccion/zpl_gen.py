################################
## Generador ZPL 
##
## Genera archivos de etiquetas zpl partiendo de un archivo CSV
## que puede ser leido de disco o de cortapapeles. La primer fila
## debe contener los tags para reemplazar en el tamplate
##
## ARGS:
## - zpl_template: Archivo a usarse de modelo que se completa con
##   los valores de los tags
## 
## --csv: Archivo CSV de entrada. De ser NULL se toma lo existente
##        en el clipboard
## --outdir: Carpeta de salida donde se graban los archivos de etiqueta generados
################################

import mod_zpl_template as mzpl
import os
import argparse
import pyperclip
import io

def save_zpl(etiqueta, out_dir):
    fn = etiqueta[1]['_idlote']
    full_path = os.path.join(out_dir, f'{fn}.zpl')    
    with open(full_path, 'w') as archivo:
        lineas = etiqueta[2].splitlines()
        for linea in lineas:
            archivo.write(linea + '\n')    
        print(f'{fn}.zpl')

parser = argparse.ArgumentParser()
# parser.add_argument('files', nargs='*', help='nombres de archivo (opcionales)')
parser.add_argument('zpl_template', help='archivo ZPL con tags a ser usado como template')
# parser.add_argument('-v', '--clipboard', action='store_true', help='tomar nombres de archivo del portapapeles')
parser.add_argument('--csv', required=False, help='archivo de entrada csv con los datos de las etiquetas. Vacío para tomar el clipboard')
parser.add_argument('-o', '--outdir', default='.', help='carpeta de salida donde se graban los archivos de etiqueta generados')
args = parser.parse_args()

zpl_file_name = args.zpl_template
out_dir = args.outdir
csv_file_name = args.csv
# clipboard = args.clipboard

# file_names = args.files
print(f'Modelo zpl: {zpl_file_name}')
print(f'Modelo carpeta de salida: {out_dir}')
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

etiquetas = mzpl.generate_zpl_content(zpl_file_name, data_dict)
print(f'Etiquetas encontradas: {len(etiquetas)}')
for etiqueta in etiquetas:
    save_zpl(etiqueta,out_dir)
