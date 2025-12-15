@echo off
title HacxGPT Installer
setlocal

echo ======================================
echo     HacxGPT Installer for Windows
echo ======================================

:: Check for Python
echo [~] Checking for Python...
python --version >nul 2>nul
if %errorlevel% neq 0 (
    echo [!] Python is not installed or not in PATH.
    echo [!] Please install Python from https://www.python.org/downloads/
    pause
    exit /b
)
echo [+] Python found.

:: Create Virtual Environment
echo [~] Creating Virtual Environment...
if not exist ".venv" (
    python -m venv .venv
    echo [+] Virtual environment created.
) else (
    echo [~] Virtual environment already exists.
)

:: Activate Virtual Environment
echo [~] Activating venv...
call .venv\Scripts\activate
if %errorlevel% neq 0 (
    echo [!] Failed to activate virtual environment.
    pause
    exit /b
)

:: Upgrade PIP
echo [~] Upgrading pip...
python -m pip install --upgrade pip

:: Install Package
echo [~] Installing HacxGPT...
pip install -e .

echo.
echo ======================================
echo       Installation Complete!
echo ======================================
echo.
echo To run HacxGPT:
echo 1. .venv\Scripts\activate
echo 2. hacxgpt
echo.
pause
