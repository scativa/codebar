import csv
# python pastetable.py > temp_table.txt; python table2label.py > temp_label.txt; lp -d zebra-raw <<< cat temp_label.txt

lote, fecha, peso_total, neto_total = 4* [""]

with open("temp_table.txt") as tsv:
    xbase = 250
    ## Código de barras
    # xstep = (40,75)
    # xstep_cb = 25
    xstep = (60,55)
    col = (55,320,540)
    print("^XA")

    print("^FX Second section: BANDEJAS: listado con pesos")
    print("^CFA,30")

    print(f"^FO{col[0]},{xbase}^FDBand^FS")
    print(f"^FO{col[1]},{xbase},1^FDPeso[gr]^FS")
    print(f"^FO{col[2]},{xbase},1^FDNeto[gr]^FS")

    xbase += xstep[0]
    header = True
    for line in csv.reader(tsv, dialect="excel-tab"): #You can also use delimiter="\t" rather than giving a dialect.
        if len(line[2]) > 0:
            if not header:
                bandeja, peso, neto = line[1], line[2], line[3]
                
                print(f"^FO{col[0]},{xbase}^FD{bandeja}^FS")
                print(f"^FO{col[1]},{xbase},1^FD{peso}^FS")
                print(f"^FO{col[2]},{xbase},1^FD{neto}^FS")
                #print(line)

                ## Código de barras por bandeja
                # print(f"^BY3,2,30")
                # print(f"^FO{col[0]},{xbase + xstep_cb}^BCN,40,N^FD{bandeja}|{lote}|{neto}^FS")

                xbase += xstep[1]
            else:
                header = False
                lote, fecha, peso_total, neto_total = line[0], line[1], line[2], line[3],
                print(lote, fecha, peso_total, neto_total)

                print("^FX CUADRO")
                print("^FO50,30^GB700,200,3^FS")
                print("^FO490,30^GB3,200,3^FS")

                print("^FX Top section: RECTIFICADOS")
                print("^CF0,190")
                print("^FO50,50^FDRECT^FS")
                print("^CFA,15")
                print(f"^FO65,200^FDRECTIFICADO {lote}^FS")

                print("^CFA,30")
                print(f"^FO520,50^FD{fecha}^FS")
                print(f"^FO520,90^FD{lote}^FS")


                print("^FX Fourth section (the two boxes on the bottom).")
                print("^FO20,1100^GB780,110,3^FS")
                print("^CF0,40")
                print("^FO35,1110^FDPeso total:^FS")
                print(f"^FO335,1110,1^FD{peso_total}^FS")
                print("^FO335,1110^FDgr^FS")
                print("^FO35,1160^FDNeto total:^FS")
                print(f"^FO335,1160,1^FD{neto_total}^FS")
                print("^FO335,1160^FDgr^FS")

                print(f"^BY3,2,270")
                print(f"^FO385,1110^BCN,90,N^FD{neto_total}^FS")


                print("^CFA,30")

    print("^XZ")






#^BY3,2,30
#^FO55,350^BCN,40,N^FDS12|L06/22|2810.5^FS

#^XZ