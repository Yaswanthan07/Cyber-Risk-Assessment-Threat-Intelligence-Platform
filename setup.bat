@echo off
REM CyberScan Pro - Setup Script for Windows
REM This script automates the setup process

echo.
echo ===========================
echo CyberScan Pro Setup
echo ===========================
echo.

REM Check Python version
echo Checking Python version...
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python is not installed or not in PATH
    echo Please install Python 3.8 or higher from https://www.python.org
    pause
    exit /b 1
)
for /f "tokens=2" %%i in ('python --version 2^>^&1') do set PYTHON_VERSION=%%i
echo Found Python %PYTHON_VERSION%
echo.

REM Create virtual environment
echo Creating virtual environment...
if not exist "venv" (
    python -m venv venv
    echo Virtual environment created
) else (
    echo Virtual environment already exists
)
echo.

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat
echo Virtual environment activated
echo.

REM Upgrade pip
echo Upgrading pip...
python -m pip install --quiet --upgrade pip
echo pip upgraded
echo.

REM Install dependencies
echo Installing Python dependencies...
pip install -r requirements.txt
echo Dependencies installed
echo.

REM Setup environment file
echo Setting up environment configuration...
if not exist ".env" (
    if exist ".env.example" (
        copy .env.example .env
        echo Created .env file from .env.example
        echo IMPORTANT: Edit .env with your API keys!
    ) else (
        echo .env.example not found
    )
) else (
    echo .env already exists
)
echo.

REM Create necessary directories
echo Creating data directories...
if not exist "scan_xml" mkdir scan_xml
if not exist "data" mkdir data
if not exist "logs" mkdir logs
echo Directories created: scan_xml\, data\, logs\
echo.

echo ===========================
echo Setup Complete!
echo ===========================
echo.
echo Next steps:
echo 1. Edit .env file with your API keys
echo 2. Run: streamlit run app.py
echo 3. Open browser to http://localhost:8501
echo.
echo For more info, see README.md
echo.
pause
