import csv
import json

def save_json(data, json_file):
    # Escribir los datos en el archivo JSON
    with open(json_file, 'w') as file:
        json.dump(data, file, indent=4)

def csv_to_json(csv_file, json_file):
    # Abrir el archivo CSV y leer los datos
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        data = [row for row in reader]

    # Escribir los datos en el archivo JSON
    with open(json_file, 'w') as file:
        json.dump(data, file, indent=4)

    # print(f"Se ha generado el archivo JSON: {json_file}")
    return data

def split_json(data, id_field,parent_key=''):
    # Toma una estructura json y guarda todos los json de primer nivel de apertura
    # si toma un dicionaro producto de csv representa un json por fila
    # basado en ./json_recursive.py
    if isinstance(data, dict):
        for key, value in data.items():
            if parent_key:
                current_key = f'{parent_key}.{key}'
            else:
                current_key = key
            # print(f'Clave: {current_key}')
            # print(f'Valor: {value}')
            # print(f'Tipo de dato: {type(value)}\n')

            # print(data[key][id_field])
            save_json(value,f"{value[id_field]}.json")

            # print(data[id_field])
    elif isinstance(data, list):
        for i, item in enumerate(data):
            # current_key = f'{parent_key}[{i}]'
            # print(f'Clave: {current_key}')
            # print(f'Valor: {item}')
            # print(f'Tipo de dato: {type(item)}\n')

            # print(item[id_field])
            save_json(item,f"{item[id_field]}.json")

if __name__ == "__main__":
    # Ejemplo de uso
    csv_file = '.\\csv\\inventario.csv'  # Ruta del archivo CSV
    json_file = './json/inventario.json'  # Ruta del archivo JSON de salida

    json_csv = csv_to_json(csv_file, json_file)
    split_json(json_csv,'_idlote')