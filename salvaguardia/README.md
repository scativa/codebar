# Salvaguardia - Generado de etiquetas
Versión especifica para impresión de etiquetas de los controles anuales de inventario de material para salvaguardia.
Queda una branch por año fijo al momento de terminar y continúa su línea independiente de la rama principal.

## Uso
Scripts bash _.sh_ para linux que permiten la generación de etiquetas y su posterior impresión. También los scripts de PowerShell (_.ps1_ y _.bat_)de Win10 sólo para la generación de etiquetas.

### Scripts para producción
[ChatGPT](https://chatgpt.com/c/5e331d27-bbba-4e2e-8413-ef946d1befe2)

**Terminal Ubuntu**
```
generar_etiquetas.sh
```

**Terminal PowerShell Windows Anaconda**
```
generar_etiquetas.ps1
```

**Ejecutar desde Explorador de Windows** (llama al archivo ps1 con entorno conda)
```
generar_etiquetas.bat
```

Genera las etiquetas en la subcarpeta *./etiquetas* a partir de el porta papeles usando como template *inventario_230623_v2.zpl_t*. Si no existe la carpeta de destino la crear, si sí existe borra todos los archivos *.zpl* que contenga.
Ejecuta`./codigos/cod_gen.py` con parámetros establecidos y comandos de consola linux.
Requiere _conda_ con python el entorno _zebra_ (ver requirements.txt)

```
imprimir_menu.sh
```
Permite seleccionar de las subcarpetas con el patron "etiquetas_*" las etiquetas a imprimir previamente generadas. Da como opción para una subcarpeta imprimir **todas** o **una en particular** 
Utiliza la impresora *zebra-raw*. No utiliza python ni precisa de entorno conda.

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
- `zpl_gen.py`: Genera el código en formato _zpl_ de etiquetas a partir de un template `.zpl` y la información un archivo `.csv` o del paste en memoria con los datos. El nombre del archivos está dado por la metadata `_idlote`. Tiene la opción de generar al momento un archivo `.json` por etiqueta con el mismo nombre.
- `./codigos/cod_gen.py`: Genera el códigos para ser usados en por los inventario compuesto de dos letras mayúsculas y un número de dos dígitos. 

## scripts (Linux y win)
[ChatGPT](https://chatgpt.com/c/5e331d27-bbba-4e2e-8413-ef946d1befe2)

## Configuración
ver _README.md_ del proyecto

## Utilidades
### Labelary
[Muestra la etiqueta a partir del código ZPL](http://labelary.com/viewer.html)
