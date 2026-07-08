@echo off
title Learnlytics - Starting...
color 0A

echo.
echo  ========================================
echo    LEARNLYTICS - Starting Servers
echo  ========================================
echo.

echo  [1/2] Starting Backend (Flask)...
start "Learnlytics Backend" cmd /k "cd /d C:\Users\sunda\Desktop\Learnlytics\backend && .\venv\Scripts\python.exe app.py"

timeout /t 4 /nobreak >nul

echo  [2/2] Starting Frontend (React)...
start "Learnlytics Frontend" cmd /k "cd /d C:\Users\sunda\Desktop\Learnlytics\frontend && npm run dev"

timeout /t 6 /nobreak >nul

echo.
echo  ========================================
echo    Both servers are starting up!
echo    Opening browser in 3 seconds...
echo  ========================================
echo.

timeout /t 3 /nobreak >nul

start "" "http://localhost:5173"

echo  Done! Browser should open automatically.
echo  Press any key to close this window.
pause >nul
