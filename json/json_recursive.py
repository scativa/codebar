import json

def read_json_recursive(data, parent_key=''):
    if isinstance(data, dict):
        for key, value in data.items():
            if parent_key:
                current_key = f'{parent_key}.{key}'
            else:
                current_key = key
            print(f'Clave: {current_key}')
            print(f'Valor: {value}')
            print(f'Tipo de dato: {type(value)}\n')
            read_json_recursive(value, current_key)
    elif isinstance(data, list):
        for i, item in enumerate(data):
            current_key = f'{parent_key}[{i}]'
            print(f'Clave: {current_key}')
            print(f'Valor: {item}')
            print(f'Tipo de dato: {type(item)}\n')
            read_json_recursive(item, current_key)

# Ejemplo de uso
json_path = 'tabla.json'  # Ruta del archivo JSON
with open(json_path, 'r') as file:
    json_data = json.load(file)

read_json_recursive(json_data)
