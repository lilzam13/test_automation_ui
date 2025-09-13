@echo off
echo ==============================
echo   Execute Robot Tests
echo ==============================

robot --listener allure_robotframework:reports/allure-results -i Login tests/test_ac.robot
allure generate reports/allure-results --clean -o reports/allure-report

echo.
echo ==============================
echo   Generate report Allure
echo ==============================

allure open reports/allure-report

pause
