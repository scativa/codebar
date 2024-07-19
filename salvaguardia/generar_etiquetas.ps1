# Activar el entorno de Conda
# & "C:\Users\<tu_usuario>\miniconda3\Scripts\conda.exe" activate zebra
& conda activate zebra

# Variables
$carpeta = "./etiquetas/"
$zpl_template = "inventario_230623_v2.zpl_t"

Write-Host "Genera etiquetas usando '$zpl_template'. Se borraran las etiquetas anteriores en la carpeta '$carpeta'"

# Verificar si la carpeta existe
if (Test-Path $carpeta) {
    Write-Host "Eliminando archivos zpl de la carpeta '${carpeta}'"
    Remove-Item "${carpeta}/*.zpl" -Force
} else {
    Write-Host "Creando carpeta de salida '${carpeta}'"
    New-Item -Path $carpeta -ItemType Directory
}

# Mensaje para copiar en el portapapeles
Read-Host -Prompt "Copie en el clipboard la planilla a generar y presione Enter para continuar..."

# Ejecutar el script de Python
python ./zpl_gen.py $zpl_template -o $carpeta

# Mensaje de finalización
Read-Host -Prompt "Finalizado. Presione Enter para continuar..."
Write-Host " "
