@echo off
setlocal
chcp 65001 >nul
cd /d "%~dp0"
title Gerador do TaskRose

echo ==========================================
echo          GERADOR DO TASKROSE.EXE
echo ==========================================
echo.

REM Procura primeiro o launcher py e depois python/python3.
set "PYTHON_CMD="
py -3 --version >nul 2>&1
if not errorlevel 1 set "PYTHON_CMD=py -3"

if not defined PYTHON_CMD (
    python --version >nul 2>&1
    if not errorlevel 1 set "PYTHON_CMD=python"
)

if not defined PYTHON_CMD (
    python3 --version >nul 2>&1
    if not errorlevel 1 set "PYTHON_CMD=python3"
)

if not defined PYTHON_CMD goto python_nao_encontrado

echo Python encontrado:
%PYTHON_CMD% --version
echo.

echo Verificando o pip...
%PYTHON_CMD% -m pip --version >nul 2>&1
if errorlevel 1 (
    echo O pip nao foi encontrado. Tentando habilita-lo...
    %PYTHON_CMD% -m ensurepip --upgrade
    if errorlevel 1 goto erro
)

echo.
echo Instalando as bibliotecas necessarias...
%PYTHON_CMD% -m pip install --upgrade pip
if errorlevel 1 goto erro
%PYTHON_CMD% -m pip install customtkinter pillow pyinstaller
if errorlevel 1 goto erro

echo.
echo Gerando o aplicativo...
%PYTHON_CMD% -m PyInstaller --noconfirm --clean --windowed --onedir --name TaskRose --icon "TaskRose.ico" --add-data "Logo TasKRose.png;." --collect-all customtkinter "TaskRose.py"
if errorlevel 1 goto erro

echo.
echo ==========================================
echo CONCLUIDO!
echo O aplicativo esta em: dist\TaskRose\TaskRose.exe
echo ==========================================
echo.
echo Envie a pasta inteira dist\TaskRose para outro computador.
pause
exit /b 0

:python_nao_encontrado
echo ERRO: Nao encontrei Python pelos comandos py, python ou python3.
echo.
echo Se o Python funciona no VS Code, confira o interpretador:
echo Ctrl+Shift+P ^> Python: Select Interpreter.
echo Se nao estiver instalado, instale pelo site python.org e marque:
echo Add python.exe to PATH.
echo Depois feche e abra novamente este arquivo BAT.
echo.
pause
exit /b 1

:erro
echo.
echo Ocorreu um erro durante a instalacao ou compilacao.
echo Confira a mensagem acima e tente novamente.
pause
exit /b 1
