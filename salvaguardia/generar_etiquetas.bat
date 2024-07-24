@echo off
REM https://chatgpt.com/c/5e331d27-bbba-4e2e-8413-ef946d1befe2

REM Verifica si se ha pasado un parámetro
REM debe ser %USERPROFILE% si conda está instalado en el usuario actual o
REM C:\ProgramData\miniconda3 si está para todo el sistema

if "%1"=="" (
    echo No se ha proporcionado el valor para conda root.
	pause
    exit /b 1

)

echo Ejecutando conda desde "%1%"

REM Usar variables de entorno para obtener las rutas correctas
REM set ANACONDA_PROMPT="%USERPROFILE%\miniconda3\shell\condabin\conda-hook.ps1"
REM set ANACONDA_PROMPT="C:\ProgramData\miniconda3\shell\condabin\conda-hook.ps1"
set ANACONDA_PROMPT="%1%\shell\condabin\conda-hook.ps1"
echo %ANACONDA_PROMPT%

set POWERSHELL_PATH="C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe"
set SCRIPT_PATH=".\generar_etiquetas.ps1"

REM Abre el Anaconda Powershell Prompt y ejecuta el script de PowerShell
%POWERSHELL_PATH% -ExecutionPolicy Bypass -NoExit -Command "& { . %ANACONDA_PROMPT%; conda activate zebra; . %SCRIPT_PATH% }"
