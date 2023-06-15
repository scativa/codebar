import json

def print_zpl_content(file_path, data_file):
    with open(file_path, 'r') as file:
        zpl_content = file.read()

    with open(data_file, 'r') as data_file:
        data = json.load(data_file)

    for marca in data:
        zpl_content = zpl_content.replace(marca, str(data[marca]))

    for line in zpl_content.splitlines():
        print(line.strip())

if __name__ == "__main__":
    # Ejemplo de uso
    modelo_path = 'modelo.zpl'
    data_path = 'data.json'
    print_zpl_content(modelo_path, data_path)
