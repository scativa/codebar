codigos = []

# Generar códigos consecutivos
for letra1 in range(ord('A'), ord('Z')+1):
    for letra2 in range(ord('A'), ord('Z')+1):
        for numero in range(10, 100):
            codigo = chr(letra1) + chr(letra2) + str(numero)
            codigos.append(codigo)

# Imprimir la lista de códigos
for codigo in codigos:
    print(codigo)
