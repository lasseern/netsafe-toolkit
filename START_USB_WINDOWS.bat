@echo off
REM ================================================
REM  All-in-One Net Safe - Portable USB Launcher
REM  Supports embedded Python and system Python
REM ================================================

SETLOCAL EnableDelayedExpansion

echo.
echo ================================================
echo  All-in-One Net Safe - USB Edition
echo ================================================
echo.

REM Get current directory
set "APP_DIR=%~dp0"
set "USB_DRIVE=%~d0"

echo USB Drive: %USB_DRIVE%
echo App Directory: %APP_DIR%
echo.

REM === Check for Portable Python (WinPython) ===
set "WINPYTHON_DIR=%USB_DRIVE%\WPy64-31"
set "PYTHON_EXE="

if exist "%WINPYTHON_DIR%\python-*.amd64\python.exe" (
    for /d %%D in ("%WINPYTHON_DIR%\python-*.amd64") do (
        if exist "%%D\python.exe" (
            set "PYTHON_EXE=%%D\python.exe"
            echo [INFO] Found Portable Python: %%D
            goto :python_found
        )
    )
)

REM === Check for System Python ===
:check_system_python
echo [INFO] Checking system Python...
where python >nul 2>nul
if %ERRORLEVEL% EQU 0 (
    set "PYTHON_EXE=python"
    echo [OK] System Python found
    goto :python_found
)

REM === No Python found ===
echo.
echo ================================================
echo  ERROR: No Python Installation Found!
echo ================================================
echo.
echo Please do ONE of the following:
echo.
echo OPTION 1 - System Python (Recommended):
echo   1. Download Python 3.8+ from https://www.python.org/
echo   2. Install with "Add Python to PATH" checked
echo   3. Rerun this script
echo.
echo OPTION 2 - Portable Python (USB Only):
echo   1. Download WinPython from https://winpython.github.io/
echo   2. Extract to: %USB_DRIVE%\WPy64-31\
echo   3. Rerun this script
echo.
pause
exit /b 1

:python_found
echo.
echo Testing Python...
"%PYTHON_EXE%" --version
if %ERRORLEVEL% NEQ 0 (
    echo [ERROR] Python test failed!
    pause
    exit /b 1
)
echo [OK] Python is working
echo.

REM === Install Dependencies ===
echo ================================================
echo  Installing Dependencies
echo ================================================
echo.
echo This may take a few minutes on first run...
echo.

"%PYTHON_EXE%" -m pip install --quiet --upgrade pip 2>nul
"%PYTHON_EXE%" -m pip install --quiet -r "%APP_DIR%requirements.txt"

if %ERRORLEVEL% NEQ 0 (
    echo.
    echo [WARNING] Some dependencies may have failed.
    echo The application will attempt to run anyway...
    echo.
) else (
    echo [OK] All dependencies installed
)

echo.

REM === Launch Application ===
echo ================================================
echo  Starting All-in-One Net Safe
echo ================================================
echo.
echo  10 Security Tools Ready:
echo  [1] Tor Routing (Nipe)
echo  [2] Transparent Proxy (Kalitorify)
echo  [3] Web Crawler (Hakrawler)
echo  [4] Dark Web OSINT (TorBot)
echo  [5] Network Pentesting (NetExec)
echo  [6] Network Forensics (BruteShark)
echo  [7] PC Information
echo  [8] Disk Benchmark
echo  [9] Network Visualizer
echo  [10] System Tools
echo.
echo ================================================
echo.

cd /d "%APP_DIR%"
set "PYTHONPATH=%APP_DIR%;%APP_DIR%\lib"
set "NETSAFE_USB_MODE=1"

"%PYTHON_EXE%" main.py

if %ERRORLEVEL% NEQ 0 (
    echo.
    echo ================================================
    echo  Application Error
    echo ================================================
    echo.
    echo Check logs in: %APP_DIR%logs\
    echo.
    pause
)

ENDLOCAL
