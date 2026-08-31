@echo off
REM Amazon UI Automation Framework - Test Runner Script for Windows

echo.
echo =========================================================
echo 🛒 Amazon UI Automation Framework - Test Runner
echo =========================================================
echo.

REM Run tests with HTML report and screenshots
echo Running tests with HTML report...
echo.

pytest tests\test_login.py -v ^
    --html=Reports\report.html ^
    --self-contained-html ^
    --tb=short

if %ERRORLEVEL% EQU 0 (
    echo.
    echo ✅ All tests passed!
    echo 📊 HTML Report: Reports\report.html
    echo 📸 Screenshots: Reports\screenshots\
) else (
    echo.
    echo ❌ Tests failed. Check report and screenshots for details.
    echo 📊 HTML Report: Reports\report.html
    echo 📸 Failed Screenshots: Reports\screenshots\
)

pause
