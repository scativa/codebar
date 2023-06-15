import json

texto_json = '{"clave1": "valor1","clave2": 42,"clave3": ["elemento1", "elemento2", "elemento3"],"clave4": {"subclave1": "subvalor1","subclave2": "subvalor2"}}'

# Cargar el string de texto como un objeto JSON
data = json.loads(texto_json)

# Escribir el objeto JSON en un archivo
nombre_archivo = 'datos.json'
with open(nombre_archivo, 'w') as archivo:
    json.dump(data, archivo, indent=4)

print(f'Se ha generado el archivo JSON: {nombre_archivo}')
