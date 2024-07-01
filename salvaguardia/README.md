# Salvaguardia - Generado de etiquetas
Versión especifica para impresión de etiquetas de los controles anuales de inventario de material para salvaguardia.
Queda una branch por año fijo al momento de terminar y continúa su línea independiente de la rama principal.

## Uso
Dos scripts de shell  _*.sh_ para linux que permiten la generación de etiquetas y su posterior impresión.

### Scripts para producción
```
generar_etiquetas.sh
```
Genera las etiquetas en la subcarpeta *./etiquetas* a partir de el porta papeles usando como template *inventario_230623_v2.zpl_t*. Si no existe la carpeta de destino la crear, si sí existe borra todos los archivos *.zpl* que contenga.
Ejecuta`./codigos/cod_gen.py` con parámetros establecidos y comandos de consola linux.
Requiere _conda_ con python el entorno _zebra_ (ver requirements.txt)

```
imprimir_etiquetas.sh
```
Imprime en *zebra-raw* las etiquetas _*.zpl_ de la subcarpeta *./etiquetas*. No utiliza código python.

### Linea de comandos
#### Generación de etiquetas
Primero se activa el entorno _zebra_
```
conda activate zebra
```
Comando para generar a partir de el porta papeles
```
python ./zpl_gen.py ./modelo.zpl -o ./out/
```
Comando para generar a partir de un _csv_
```
python ./zpl_gen.py ./modelo.zpl -o ./out/ --csv ./csv/inventario.csv
```
#### Impresión de etiquetas
Imprime en el dispositivo __zebra-raw__ en ubuntu. [ChatGPT](https://chat.openai.com/c/4736aef4-f2ee-4197-9721-cee293930aa6)

Para una etiqueta específica
```
lp -d zebra-raw <<< cat label.zpl
```
Para todas las etiquetas de la carpeta
```
for file in *.zpl; do lp -d zebra-raw <<< "$(cat "$file")"; done
```

Versión anterior que utiliza código python para generar un archivo zpl con la información a imprimir. Quedó en el branch `CodeGenVersion`.


## Files
- `mod_zpl_template.py`: Copia de existente en la raiz del proyecto.
- `zpl_gen.py`: Genera el código en formato _zpl_ de etiquetas a partir de un template `.zpl` y la información un archivo `.csv` o del paste en memoria con los datos. El nombre del archivos está dado por la metadata `_idlote`
- `./codigos/cod_gen.py`: Genera el códigos para ser usados en por los inventario compuesto de dos letras mayúsculas y un número de dos dígitos. 

__Carpetas__
- `./producción`: Estructura y archivos para .
- `./etiquetas`: Carpeta con archivos de salida, generalmente _zpl_. No se mantienen los cambios en _git_.
- `./csv`: Carpeta con archivos _csv_ usados para el ingreso de datos
- `./zpl`: Carpeta con archivos _zpl_, principalmente los templates

## Configuración
ver _README.md_ del proyecto

## Utilidades
### Labelary
[Muestra la etiqueta a partir del código ZPL](http://labelary.com/viewer.html)
