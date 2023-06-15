import json

def print_zpl_content(modelo_zpl_path, data_json_path):
    with open(modelo_zpl_path, 'r') as file:
        zpl_content = file.read()

    with open(data_json_path, 'r') as data_file:
        data = json.load(data_file)

    for marca in data:
        zpl_content = zpl_content.replace(marca, str(data[marca]))

    for line in zpl_content.splitlines():
        print(line.strip())

if __name__ == "__main__":
    # Ejemplo de uso
    modelo_zpl_path = 'modelo.zpl'
    data_json_path = 'tabla.json'
    print_zpl_content(modelo_zpl_path, data_json_path)
