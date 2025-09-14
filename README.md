### ROBOT FRAMEWORK ###
*** Steps: ***
Create virtual enviroment:
python -m venv venv
venv\Scripts\activate

*** Install libraries: ***
pip install allure-robotframework
pip install robotframework-requests
pip install selenium
pip install robotframework
pip install robotframework-seleniumlibrary
pip install --upgrade robotframework-seleniumlibrary
pip install webdriver-manager
Select Interpete

 ### INSTRUCTIONS ###
*** Execute tests: ***
Execute tests: robot --listener allure_robotframework:reports/allure-results -i Login tests/test_ac.robot
Execute tests by tags: robot --listener allure_robotframework:reports/allure-results -i Login tests/test_ac.robot
*** Generate report: ***
allure generate reports/allure-results --clean -o reports/allure-report
allure open reports/allure-report

*** BUG TRACK INCIDENT QA ***
https://docs.google.com/spreadsheets/d/1uL0kWWJ5SG7nc_WebRw_kjVC1T0wZ9yw7NBrBcqpNVk/edit?gid=0#gid=0



