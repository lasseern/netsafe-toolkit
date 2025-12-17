@echo off
REM Portable Launcher for Windows

echo ================================================
echo  All-in-One Net Safe - Portable Windows Launcher
echo ================================================
echo.

REM Tjek om Python er installeret
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Python er ikke installeret!
    echo.
    echo Download Python fra: https://www.python.org/downloads/
    echo Husk at vælge "Add Python to PATH" under installation
    pause
    exit /b 1
)

REM Få script directory
set SCRIPT_DIR=%~dp0
cd /d "%SCRIPT_DIR%"

echo Python fundet!
echo Working directory: %SCRIPT_DIR%
echo.

REM Tjek om requirements er installeret
python -c "import customtkinter" >nul 2>&1
if %errorlevel% neq 0 (
    echo Installerer dependencies...
    python -m pip install --user -r requirements.txt
    if %errorlevel% neq 0 (
        echo.
        echo ERROR: Kunne ikke installere dependencies
        pause
        exit /b 1
    )
)

echo.
echo Starting All-in-One Net Safe...
echo.

REM Start programmet
python portable_launcher.py

if %errorlevel% neq 0 (
    echo.
    echo Program afsluttet med fejl
    pause
)
