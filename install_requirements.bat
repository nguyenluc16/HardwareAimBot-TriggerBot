@echo off
title Installing Python dependencies...
echo ==============================
echo  Installing dependencies...
echo ==============================
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

if %errorlevel% neq 0 (
    echo.
    echo Installation failed.
    pause
    exit /b %errorlevel%
)

echo.
echo All dependencies installed successfully.
pause
