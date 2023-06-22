import json
import csv
# https://chat.openai.com/c/64f4dc11-522e-4ad1-8f10-6e7b429ff514
# Partiendo de un archivo CSV (el delimitador se pasa como parámetro) se lo lee como una estructura de diccionario
# Este lo convierte a archivo json

def csv_to_json(csv_file, json_file, delimiter=','):
    # Abrir el archivo CSV y leer los datos
    # with open(csv_file, 'r') as file:
    reader = csv.DictReader(csv_file, delimiter=delimiter)
    data = [row for row in reader]

    # Escribir los datos en el archivo JSON
    with open(json_file, 'w') as file:
        json.dump(data, file, indent=4)

    print(f"Se ha generado el archivo JSON: {json_file}")


def print_zpl_content(modelo_zpl_path, data_json_path):
    with open(data_json_path, 'r') as data_file:
        json_data = json.load(data_file) # Empieza con una lista

    for i, etiqueta in enumerate(json_data):

        with open(modelo_zpl_path, 'r') as file:
            zpl_template = file.read()

        print(f'^FX --- Etiqueta {i} ---')
        for marca in etiqueta:
            zpl_template = zpl_template.replace(marca, str(etiqueta[marca]))

        for line in zpl_template.splitlines():
            print(line.strip())

if __name__ == "__main__":
    # Ejemplo de uso
    csv_file_name = './csv/inventario.csv'  # Ruta del archivo CSV
    json_file_name = './json/inventario.json'  # Ruta del archivo JSON de salida

    with open(csv_file_name, 'r') as csv_file:
        csv_to_json(csv_file, json_file_name)

    zpl_file_name = './zpl/inventario_SHORT.zpl'
    # data_json_path = './json/inventario.json'
    print_zpl_content(zpl_file_name, json_file_name)
