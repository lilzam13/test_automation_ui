### ROBOT FRAMEWORK </br>
*** Steps: ***</br>
Create virtual enviroment:</br>
python -m venv venv</br>
venv\Scripts\activate</br>

*** Install libraries: ***</br>
pip install allure-robotframework</br>
pip install robotframework-requests</br>
pip install selenium</br>
pip install robotframework</br>
pip install robotframework-seleniumlibrary</br>
pip install --upgrade robotframework-seleniumlibrary</br>
pip install webdriver-manager</br>
Select Interpete</br>

 ### INSTRUCTIONS </br>
*** Execute tests: ***</br>
Execute tests: robot --listener allure_robotframework:reports/allure-results -i Login tests/test_ac.robot</br>
Execute tests by tags: robot --listener allure_robotframework:reports/allure-results -i Login tests/test_ac.robot</br>
*** Generate report: ***</br>
allure generate reports/allure-results --clean -o reports/allure-report</br>
allure open reports/allure-report</br>

*** BUG TRACK ***</br>
https://docs.google.com/spreadsheets/d/1uL0kWWJ5SG7nc_WebRw_kjVC1T0wZ9yw7NBrBcqpNVk/edit?gid=0#gid=0</br>



