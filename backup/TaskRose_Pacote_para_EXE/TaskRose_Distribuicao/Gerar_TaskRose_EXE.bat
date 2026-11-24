@echo off
chcp 65001 >nul
cd /d "%~dp0"
echo ==========================================
echo          GERADOR DO TASKROSE.EXE
echo ==========================================
echo.

py -m pip install --upgrade pip
if errorlevel 1 goto erro

py -m pip install customtkinter pillow pyinstaller
if errorlevel 1 goto erro

echo.
echo Gerando o aplicativo...
py -m PyInstaller --noconfirm --clean --windowed --onedir --name TaskRose --icon "TaskRose.ico" --add-data "Logo TasKRose.png;." --collect-all customtkinter "TaskRose.py"
if errorlevel 1 goto erro

echo.
echo ==========================================
echo CONCLUIDO!
echo O aplicativo esta em: dist\TaskRose\TaskRose.exe
echo ==========================================
pause
exit /b 0

:erro
echo.
echo Ocorreu um erro. Confira se o Python esta instalado e disponivel pelo comando py.
pause
exit /b 1
