# https://chatgpt.com/c/5e331d27-bbba-4e2e-8413-ef946d1befe2
# Generar un número aleatorio de seis dígitos
$randomNumber = Get-Random -Minimum 1000 -Maximum 9999

# Prefijo de la carpeta
$prefix = "etiquetas_"

# Nombre de la carpeta
$folderName = "$prefix$randomNumber"

# Activar el entorno de Conda
# & "C:\Users\<tu_usuario>\miniconda3\Scripts\conda.exe" activate zebra
& conda activate zebra

# Variables
$carpeta = "./$folderName/"
$zpl_template = "inventario_230623_v2.zpl_t"

Write-Host "Genera etiquetas usando '$zpl_template'"

# Verificar si la carpeta existe
if (Test-Path $carpeta) {
    Write-Host 
    Read-Host -Prompt "Se borraran las etiquetas anteriores en la carpeta '$carpeta'. Presione Enter para continuar..."

    Write-Host "Eliminando archivos zpl de la carpeta '${carpeta}'"
    Remove-Item "${carpeta}/*.zpl" -Force
} else {
    Write-Host "Creando carpeta de salida '${carpeta}'"
    New-Item -Path $carpeta -ItemType Directory > $null
}

# Mensaje para copiar en el portapapeles
Read-Host -Prompt "Copie en el clipboard la planilla a generar y presione Enter para continuar..."

# Ejecutar el script de Python
python ./zpl_gen.py $zpl_template -o $carpeta

# Mensaje de finalización
Write-Host "----------------------------------------"
Write-Host "- Carpeta: $folderName"
Write-Host "----------------------------------------"
Read-Host -Prompt "Finalizado. Presione Enter para continuar..."
Write-Host " "
