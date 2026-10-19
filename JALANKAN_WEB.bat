@echo off
title Server Web SOP Toko Komputer, Aksesori, dan Servis
cd /d "%~dp0"

where python >nul 2>nul
if %ERRORLEVEL% EQU 0 (
    echo Menjalankan Server Python SOP Toko...
    python app.py
    pause
    exit /b
)

where py >nul 2>nul
if %ERRORLEVEL% EQU 0 (
    echo Menjalankan Server Python SOP Toko...
    py app.py
    pause
    exit /b
)

echo =================================================================
echo Python belum terdeteksi di PATH komputer ini.
echo Membuka aplikasi Web SOP secara langsung di Browser...
echo =================================================================
start "" "%~dp0index.html"
