import os
import datetime
from selenium import webdriver

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

# Configura las opciones para ejecutar Chrome en modo headless
options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

# Inicializa el driver. Selenium Manager se encargará de encontrar el driver compatible.
# Ya no es necesario el objeto Service ni la ruta del driver.
driver = webdriver.Chrome(options=options)
# ... tu código de automatización ...

driver.quit()

class Inicializar():

    # Ruta absoluta al directorio base del proyecto
    BASEDIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

    # Ruta a la carpeta de drivers
    DRIVERS_DIR = os.path.join(BASEDIR, "src", "drivers")

    # Ruta a la carpeta de pages
    PAGES_DIR = os.path.join(BASEDIR, "src", "pages")
    
    #Directorio de evidencia
    path_evidencias = os.path.join(BASEDIR, "src", "data","capturas")

    #Hoja de datos excel
    Excel = os.path.join(BASEDIR, "src", "data","Data_Test.xlsx")

    DateFormat = '%m/%d/%Y'
    HourFormat = '%I:%M:%S'

    #Browser de pruebas
    NAVEGADOR = 'CHROME'

    Enviroment =  'Test'

    if Enviroment == "Dev":
        URL = 'https://www.google.com/'
        User = "lilian"
        Pass = "Stx12345$"
        Scenario = {
            "ENV_ID": "74",
            "TBASE": "BASE DEV Liliana",
            "Proceso": "Review170",
            "email":"lilianazam13@gmail.com"
        }
        DB_HOST = "127.0.0.1"
        DB_PORT = "3306"
        DB_DATABASE = "world"
        DB_USER = "root"
        DB_PASS = "stx123"


    if Enviroment == "Test":
        URL = 'https://www.facebook.com/r.php?entry_point=login'
        User = "lilzam"
        Pass = "Stx54321$"

        Scenario = {
            "ENV_ID": "74",
            "TBASE": "BASE TEST Liliana",
            "Proceso": "Review170",
            "email":"lilianaqa@gmail.com"
        }
        DB_HOST = "127.0.0.1"
        DB_PORT = "3306"
        DB_DATABASE = "world"
        DB_USER = "root"
        DB_PASS = "stx123"

if __name__ == "__main__":
    print("Inicializando configuración...")
    config = Inicializar()
    print("URL de pruebas:", config.URL)
