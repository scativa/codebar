 # codebar
Genera e imprime por linea de comandos etiquetas para las impresoras térmicas __Zebra GC420t__. Estas se generan a partir de un template `.zpl` que se completa con la información en formato dict proveniente de un archivo `.json`, `.csv` o del portapapeles con los datos.

## Files
- `mod_zpl_template.py`: Librería para generar a partir de un template `.zpl`, usando la información almacenada diccionarios `type(dict)`. Provee herramientas para genera los diccionarios partiendo de _csv_, _json_ y ejemplos para tomar el desde _clipboard_.
- `json2label.py`: Genera el código en formato _zpl_ de etiquetas a partir de un template `.zpl` y la información un archivo `.json` con los datos.
- `zpl_gen.py`: Genera el código en formato _zpl_ de etiquetas a partir de un template `.zpl` y la información un archivo `.csv` o del paste en memoria con los datos. Está especificado para el manejo de salvaguardia, ya que los nombres de archivo están dados por la metadata `_idlote`
- `./csv`: Carpeta con código ejemplo de formato _csv_
- `./json`: Carpeta con código ejemplo de manejo de archivos y formato _json_
- `./zpl`: Carpeta con archivos y código ejemplo de manejo de formato _zpl_

## Configuración
```
conda create -n  zebra python=3.10.4
conda activate zebra
python -m pip install -r requirements.txt 
```
```
sudo apt install xclip 
```

## GIT
[Configuración proxy para CNEA](https://docs.google.com/document/d/1PBPeE-3_t7xeguKVyJ43NtW8PBHgLuLB9SqO0_dvmN0/edit#heading=h.bbutr3mgg8o5)

## Uso
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

### ChatGPT
[Zebra Print](https://chat.openai.com/c/64f4dc11-522e-4ad1-8f10-6e7b429ff514)
[Print .zpl files batch](https://chat.openai.com/c/4736aef4-f2ee-4197-9721-cee293930aa6)

### Documentación Adicional
[Versión Google Docs](https://docs.google.com/document/d/1KEMTndB9a6GAG9w_y4i5BaqnAcqN8ZQys83Q_9N4GOU/edit?usp=sharing)
### Zebra
[“print zpl from java” Code Answer](https://www.codegrepper.com/code-examples/java/print+zpl+from+java)

## Utilidades
### Labelary
[Muestra la etiqueta a partir del código ZPL](http://labelary.com/viewer.html)

### Node js
[ZPL Packages](ttps://npm.io/search/keyword:ZPL)
[Use the SendFileToPrinter API for Your Cloud-Based Printing Needs - Zebra Developer Portal](https://npm.io/search/keyword:ZPL)
jszpl - Generate ZPL II from JavaScript
[node](https://www.npmjs.com/package/jszpl?activeTab=readme)


### Información a revisar
La siguiente información precisa ser revisada para verificar su utilidad actual
[zebra-printer - Github](https://github.services.devops.takamol.support/topics/zebra-printer)

[Xenops v1.12 / ZPL Label Templates System / User's Guide](https://github.com/latitov/ZPL-Label-Templates)

### Python PCL / ZPL
Permite impresión en zebra-raw (texto en francés)
https://github.com/mchobby/PythonPcl
https://github.com/mchobby/PythonPcl/blob/master/test/test-printer/zebra/demo-zebra-raw-queue-cups.pdf

#### Uso?
```
cat demo.zpl > /dev/usb/lp0
lp -d zebra-raw demo.zpl
git clone https://github.com/scativa/PythonPcl
```

### zebra 0.1.0 - pypi.org
A package to communicate with (Zebra) label printers
https://pypi.org/project/zebra/
contiene la explicación sobre como instalar paquetes
https://packaging.python.org/en/latest/tutorials/installing-packages/#installing-from-pypi

### Python zebra Examples
https://python.hotexamples.com/examples/zebra/-/zebra/python-zebra-function-examples.html

### Zebra.com
Using the ZPL Command ~DY to print a PNG Monochrome Graphic on a label
Printing a PNG graphic on a label using the ZPL command ~DY
https://www.zebra.com/us/en/support-downloads/knowledge-articles/using-the-zpl-command-dy-to-print-a-png-monochrome-graphic-on-a-label.html

