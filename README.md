# codebar

## Usage
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


## Notas
[Versión Google Docs](https://docs.google.com/document/d/1KEMTndB9a6GAG9w_y4i5BaqnAcqN8ZQys83Q_9N4GOU/edit?usp=sharing)

## Zebra
[“print zpl from java” Code Answer](https://www.codegrepper.com/code-examples/java/print+zpl+from+java)

## Utilidades
### Labelary
[Muestra la etiqueta a partir del código ZPL](http://labelary.com/viewer.html)

### Node js
[ZPL Packages](ttps://npm.io/search/keyword:ZPL)
[Use the SendFileToPrinter API for Your Cloud-Based Printing Needs - Zebra Developer Portal](https://npm.io/search/keyword:ZPL)
jszpl - Generate ZPL II from JavaScript
[node](https://www.npmjs.com/package/jszpl?activeTab=readme)


### ?? 
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

