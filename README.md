# codebar
Genera e imprime por linea de comandos etiquetas para las impresoras térmicas __Zebra GC420t__. Estas se generan a partir de un template `.zpl` que se completa con la información un archivo `.json` con los datos.

Queda por desarrollar los códigos que a partir de una o más lineas de planillas de cálculo del clipboard generen las etiquetas y estas sean impresas por lineas de comando. Esto se había logrado en la versión anterior `CodeGenVersion`

## Files
- `mod_zpl_template.py`: Genera el código en formato _zpl_ de etiquetas a partir de un template `.zpl` y la información un archivo `.csv` o del paste en memoria con los datos. Es una librería para ser usada en desarrollos variados.
- `json2label.py`: Genera el código en formato _zpl_ de etiquetas a partir de un template `.zpl` y la información un archivo `.json` con los datos.
- `./csv`: Carpeta con código ejemplo de formato _csv_
- `./json`: Carpeta con código ejemplo de manejo de archivos y formato _json_
- `./zpl`: Carpeta con archivos y código ejemplo de manejo de formato _zpl_

## Old
Versión anterior que utiliza código python para generar un archivo zpl con la información a imprimir. Quedó en el branch `CodeGenVersion`


```
conda create -n  zebra python=3.10.4
conda activate zebra
python -m pip install -r requirements.txt 
```


## Usage
```
conda activate zebra
python ./zpl_gen.py ./zpl/inventario_230623_v1.zpl -o ./out/
```

```
lp -d zebra-raw <<< cat label.zpl
```

```
conda activate zebra
python pastetable.py > temp_table.txt
python table2label.py > temp_label.zpl
lp -d zebra-raw <<< cat temp_label.zpl
```

# Paste

## Linux
```
sudo apt install xclip 
```

## Documentación complementaria
### ChatGPT
[ChatGPT](https://chat.openai.com/c/64f4dc11-522e-4ad1-8f10-6e7b429ff514)
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

