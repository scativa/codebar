# Inventario - Generado de etiquetas
Genera e imprime por linea de comandos etiquetas para las impresoras térmicas __Zebra GC420t__. Estas se generan a partir de un template `.zpl` que se completa con la información un archivo `.json` con los datos.
Está línea está adaptada a las etiquetas de inventario y continúa su línea independiente de la rama principal.


## Files
- `mod_zpl_template.py`: Librería para generar a partir de un template `.zpl`, usando la información almacenada diccionarios `type(dict)`. Provee herramientas para genera los diccionarios partiendo de _csv_, _json_ y ejemplos para tomar el desde _clipboard_.
- `zpl_gen.py`: Genera el código en formato _zpl_ de etiquetas a partir de un template `.zpl` y la información un archivo `.csv` o del paste en memoria con los datos. El nombre del archivos está dado por la metadata `_idlote`
- `cod_gen.py`: Genera el códigos para ser usados en por los inventario compuesto de dos letras mayúsculas y un número de dos dígitos. 

- `./out`: Carpeta con archivos de salida, generalmente _zpl_. No se mantienen los cambios en _git_.
- `./csv`: Carpeta con archivos _csv_ usados para el ingreso de datos
- `./zpl`: Carpeta con archivos _zpl_, principalmente los templates

## Configuración
```
conda create -n  zebra python=3.10.4
conda activate zebra
python -m pip install -r requirements.txt 
```
```
sudo apt install xclip 
```

## Usage
### Generación de etiquetas
Primero se activa el entorno _zebra_
```
conda activate zebra
```
Comando para generar a partir de el porta papeles
```
python ./zpl_gen.py ./zpl/modelo.zpl -o ./out/
```
Comando para generar a partir de un _csv_
```
python ./zpl_gen.py ./zpl/modelo.zpl -o ./out/ --csv inventario.csv
```
### Impresión de etiquetas
Imprime en el dispositivo __zebra-raw__ en ubuntu. [ChatGPT](https://chat.openai.com/c/4736aef4-f2ee-4197-9721-cee293930aa6)

Para una etiqueta específica
```
lp -d zebra-raw <<< cat label.zpl
```
Para todas las etiquetas de la carpeta
```
for file in *.zpl; do lp -d zebra-raw <<< "$(cat "$file")"; done
```

Versión anterior que utiliza código python para generar un archivo zpl con la información a imprimir. Quedó en el branch `CodeGenVersion`. Está en la carpeta `cmdshell`

## Utilidades
### Labelary
[Muestra la etiqueta a partir del código ZPL](http://labelary.com/viewer.html)
