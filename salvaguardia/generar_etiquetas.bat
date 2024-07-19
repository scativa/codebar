@echo off
REM Usar variables de entorno para obtener las rutas correctas
REM set ANACONDA_PROMPT="%USERPROFILE%\miniconda3\shell\condabin\conda-hook.ps1"
set ANACONDA_PROMPT="C:\ProgramData\miniconda3\shell\condabin\conda-hook.ps1"

set POWERSHELL_PATH="C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe"
set SCRIPT_PATH=".\generar_etiquetas.ps1"

REM Abre el Anaconda Powershell Prompt y ejecuta el script de PowerShell
%POWERSHELL_PATH% -ExecutionPolicy Bypass -NoExit -Command "& { . %ANACONDA_PROMPT%; conda activate zebra; . %SCRIPT_PATH% }"
