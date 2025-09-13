### ROBOT FRAMEWORK ###
pip install selenium
pip install robotframework
pip install robotframework-seleniumlibrary
pip install --upgrade robotframework-seleniumlibrary
pip install webdriver-manager

Para excel
pip install robotframework-datadriver
pip install robotframework-datadriver[XLS]

.\venv\Scripts\python.exe -m pip install robotframework
robotframework                 7.3.2
robotframework-pythonlibcore   4.4.1
robotframework-seleniumlibrary 6.7.1
req
Plugin: Robot Framework Language Server
Tipo id= #userName o input#userName

Tipo css= .mr-sm-2 o  .form-control o input.form-control o textarea.form-control

Por tipo: [type='email'] o input[type='email']
Econtrar un elemento tipo input donde el id sea userName y el type se Text= input#userName[type='text']

Xpath: //button[@id='submit'] o //button[@type='button']
or = //input[@id='userName' or @type='text']
and =  //input[@id='userName' and @type='text']
por texto= //h1[text()='Text Box'] or //span[text()='Dynamic Properties']
Coincidencia= //span[contains(text(),'Box')] or //span[contains(text(),'Links')]

Cambiar la direccion de los reportes:
robot -d C:\Users\lilia\Desktop\python-robot\reports\reports_robot .\Test_uno.robot
Correr por test cases por names similares: robot -d ..\reports\reports_robot  .\Test_practi*.robot
Correr por tags: robot -d ..\reports\reports_robot -i Test_6.3  .\Test_seis.robot

ibm: Stx_1234567$

*** Para trabajar con Apis ***
pip install requests
pip install robotframework-requests
pip install robotframework-jsonlibrary
pip install jsonpath_rw
pip install jsonpath_rw_ext

get: obtener informacion
post: insert informacion
put y patch: para actualizar
delete: para eliminar

*** Para trabajar con Base de datos ***
pip install robotframework-databaselibrary
CREATE TABLE IF NOT EXISTS pet (id INT NOT NULL AUTO_INCREMENT, name VARCHAR(100) NOT NULL, type VARCHAR(100) NOT NULL, PRIMARY KEY (id))
INSERT INTO `personas1` (`id`, `name`, `last_name1`, `last_name2`) VALUES (NULL, 'Rodrigo', 'Zamora', 'Cardenas');
SELECT name FROM personas1 WHERE name='Damian'
 UPDATE personas1 SET name='Rogelio' WHERE id=2

*** Para ejecutar casos de prueba en paralelo ***
Ejecutar casos de prueba en paralelo
pip install robotframework-pabot
pabot --processes 2 --outputdir Resultados prueba*.robot


### Allure con Robot
pip install allure-robotframework
pip install robotframework-requests
robot --listener allure_robotframework:../reports/allure-re ./practica_test2.robot
allure serve ../reports/allure-results

robot -d ..\reports\reports_robot -i Login  .\tests\test_ac.robot
robot --listener allure_robotframework:../reports/allure-report -i Login  .\test_ac.robot



Steps:
Create virtual enviroment:
python -m venv venv
venv\Scripts\activate

Install libraries:
pip install allure-robotframework
pip install robotframework-requests
pip install selenium
pip install robotframework
pip install robotframework-seleniumlibrary
pip install --upgrade robotframework-seleniumlibrary
pip install webdriver-manager
Select Interpete

Execute tests:
Execute tests: robot --listener allure_robotframework:reports/allure-results -i Login tests/test_ac.robot
Execute tests by tags: robot --listener allure_robotframework:reports/allure-results -i Login tests/test_ac.robot

Generate report:
allure generate reports/allure-results --clean -o reports/allure-report
allure open reports/allure-report



