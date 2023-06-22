import csv
import json

def csv_to_json(csv_file, json_file):
    # Abrir el archivo CSV y leer los datos
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        data = [row for row in reader]

    # Escribir los datos en el archivo JSON
    with open(json_file, 'w') as file:
        json.dump(data, file, indent=4)

    print(f"Se ha generado el archivo JSON: {json_file}")

# Ejemplo de uso
csv_file = './csv/inventario.csv'  # Ruta del archivo CSV
json_file = './json/inventario.json'  # Ruta del archivo JSON de salida

csv_to_json(csv_file, json_file)
