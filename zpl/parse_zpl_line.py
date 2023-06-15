import re

def parse_zpl_line(line):
    # Buscar las coordenadas X e Y utilizando una expresión regular
    match = re.search(r'FO(\d+),(\d+)', line)
    if match:
        x = int(match.group(1))
        y = int(match.group(2))
        return x, y
    else:
        return None

# Ejemplo de uso
zpl_line = "^FO100,200^A0N,50,50^FDHello, World!^FS"
coordinates = parse_zpl_line(zpl_line)
if coordinates:
    x, y = coordinates
    print("Coordenada X:", x)
    print("Coordenada Y:", y)
else:
    print("No se encontraron coordenadas en la línea.")
