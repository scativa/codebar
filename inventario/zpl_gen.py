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

parser = argparse.ArgumentParser()
# parser.add_argument('files', nargs='*', help='nombres de archivo (opcionales)')
parser.add_argument('zpl_template', help='archivo ZPL')
# parser.add_argument('-v', '--clipboard', action='store_true', help='tomar nombres de archivo del portapapeles')
parser.add_argument('--csv', required=False, help='archivo csv con los datos de las etiquetas')
parser.add_argument('-o', '--outdir', default='.', help='carpeta de salida para los resultados')
args = parser.parse_args()

zpl_file_name = args.zpl_template
out_dir = args.outdir
csv_file_name = args.csv
# clipboard = args.clipboard

# file_names = args.files
print(f'{zpl_file_name}, {out_dir}, {csv_file_name}')


# Ejemplo de uso
# csv_file_name = './csv/inventario.csv'  # Ruta del archivo CSV
# zpl_file_name = './zpl/inventario_SHORT.zpl'
# out_dir = './zpl/'
# data_json_path = './json/inventario.json'

# Lectura de CSV directo a dict
if csv_file_name is None:
    paste = pyperclip.paste()
    csv_file = io.StringIO(paste)
    data_dict = mzpl.csv_to_dict(csv_file, delimiter='\t')
else:
    with open(csv_file_name, 'r') as csv_file:
        data_dict = mzpl.csv_to_dict(csv_file, delimiter=',')

# # Pegado de CSV de porta papeles
# paste = pyperclip.paste()
# csv_file = io.StringIO(paste)
# data_paste = mzpl.csv_to_dict(csv_file, delimiter='\t')

etiquetas = mzpl.generate_zpl_content(zpl_file_name, data_dict)

for etiqueta in etiquetas:
    save_zpl(etiqueta,out_dir)
