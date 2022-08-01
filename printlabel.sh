conda activate zebra
python pastetable.py > temp_table.txt
python table2label.py > temp_label.zpl
lp -d zebra-raw <<< cat temp_label.zpl
