@echo off
title Cambridge B1 Preliminary Practice Web App
echo ========================================================
echo   CAMBRIDGE B1 PRELIMINARY (PET) MASTER - WEB APP
echo ========================================================
echo.
echo Dang khoi dong may chu web va mo trinh duyet...
echo.

start "" "http://localhost:8080"
python -m http.server 8080

pause
