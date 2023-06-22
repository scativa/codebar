import json
import csv
import io
import pyperclip

# https://chat.openai.com/c/64f4dc11-522e-4ad1-8f10-6e7b429ff514
# Genera por salida de pantalla las etiquetas siguiendo un formato (inventario.zpl), donde las marcas están como key en un diccionario
# este diccionario puede ser leido tanto de un csv (ver el delimitador), pasando o no por un json, como copiado del portapapeles
# Hay que prestar atención porque el que no pasa por json no admite cabecera NONE (vacía) y hace de esta una lista. 
# Debe suceder algo similar con las cabeceras repetidas

# queda parametrizar el método (paste o csv) así como el modelo. También separar las etiquetas y ver cómo se imprimen

def csv_to_jsonfile(csv_file, json_file, delimiter=','):
    # Abrir el archivo CSV y leer los datos
    reader = csv.DictReader(csv_file, delimiter=delimiter)
    data = [row for row in reader]

    # Escribir los datos en el archivo JSON
    with open(json_file, 'w') as file:
        json.dump(data, file, indent=4)

    print(f"Se ha generado el archivo JSON: {json_file}")

def csv_to_dict(csv_file, delimiter=','):
    # Abrir el archivo CSV y leer los datos
    # with open(csv_file, 'r') as file:
    reader = csv.DictReader(csv_file, delimiter=delimiter)
    data = [row for row in reader]

    return data

def print_zpl_content(modelo_zpl_path, data_list):
    for i, etiqueta in enumerate(data_list):

        with open(modelo_zpl_path, 'r') as file:
            zpl_template = file.read()

        print(f'^FX --- Etiqueta {i} ---')
        for marca in etiqueta:
            if not marca is None:
                zpl_template = zpl_template.replace(marca, str(etiqueta[marca]))

        for line in zpl_template.splitlines():
            print(line.strip())

if __name__ == "__main__":
    # Ejemplo de uso
    csv_file_name = './csv/inventario.csv'  # Ruta del archivo CSV
    json_file_name = './json/inventario.json'  # Ruta del archivo JSON de salida
    zpl_file_name = './zpl/inventario_SHORT.zpl'
    # data_json_path = './json/inventario.json'

    # Lectura de CSV a dict pasando por formato json    
    with open(csv_file_name, 'r') as csv_file:
        csv_to_jsonfile(csv_file, json_file_name)

    with open(json_file_name, 'r') as data_file:
        data_json = json.load(data_file)

    # Lectura de CSV directo a dict
    with open(csv_file_name, 'r') as csv_file:
        data_dict = csv_to_dict(csv_file, delimiter=',')

    # Pegado de CSV de porta papeles
    paste = pyperclip.paste()
    csv_file = io.StringIO(paste)
    data_paste = csv_to_dict(csv_file, delimiter='\t')

    print("data_json")
    print_zpl_content(zpl_file_name, data_json)
    print("data_dict")
    print_zpl_content(zpl_file_name, data_dict)
    print("data_paste")
    print_zpl_content(zpl_file_name, data_paste)
