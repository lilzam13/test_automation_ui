from src.main import Inicializar
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as OpcionsChrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException, NoSuchElementException, NoAlertPresentException, NoSuchWindowException, WebDriverException
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import os
import json
import pytest
import time
import datetime
import openpyxl
import pyodbc
import re
import allure
Scenario = {}

class Functions(Inicializar):
    horaGlobal = time.strftime(Inicializar.HourFormat)
    def abrir_navegador(self, URL=Inicializar.URL, navegador=Inicializar.NAVEGADOR):
        print("Directorio base: ", Inicializar.BASEDIR)
        self.ventanas = {}
        print("---------------")
        print(navegador)
        print("---------------")
    
        if navegador.upper() == ("CHROME"):
            try:
                options = OpcionsChrome()
                options.add_argument("--start-maximized")
                service = Service(executable_path=ChromeDriverManager().install())
                self.driver = webdriver.Chrome(service=service, options=options)
                self.driver.implicitly_wait(10)
                self.driver.get(URL)
                #ventanas
                self.principal = self.driver.window_handles[0]
                self.ventanas = {'Principal':self.driver.window_handles[0]}
                print("Driver inicializado correctamente")
                return self.driver
            except WebDriverException as e:
                raise RuntimeError(f"No se puede inciar el driver de Chrome {e}")
        
        if navegador.upper() == ("FIREFOX"):
            try:
                self.driver = webdriver.Firefox()
                self.driver.implicitly_wait(10)
                self.driver.maximize_window()
                self.driver.get(URL)
                service = Service(executable_path=GeckoDriverManager().install())
                self.principal = self.driver.window_handles[0]
                self.ventanas = {'Principal':self.driver.window_handles[0]}
                print("Driver inicializado correctamente")
                return self.driver
            except WebDriverException as e:
                raise RuntimeError(f"No se puede inciar el driver de Firefox {e}")
        
        if navegador.upper() == ("EDGE"):
             try:
                options = EdgeOptions()
                options.add_argument("--start-maximized")
                service = EdgeService(executable_path=EdgeChromiumDriverManager().install())
                self.driver = webdriver.Edge(service=service, options=options)
                self.driver.implicitly_wait(10)
                self.driver.get(URL)
                self.principal = self.driver.window_handles[0]
                self.ventanas = {'Principal': self.driver.window_handles[0]}
                print("Driver inicializado correctamente")
                return self.driver
             except WebDriverException as e:
                 raise RuntimeError(f"No se puede inciar el driver de Edge {e}")
                 
    def tearDown(self):
        print("Se cerrara el driver")
        self.driver.quit()


    ############################
    ###### LOCATORS HANDLE #####
    ############################

    def xpath_element(self, XPATH):
        elements = self.driver.find_element(By.XPATH, XPATH)
        print("Xpath_Elements: Se interactuo con el elemento " + XPATH)
        return elements
    def name_element(self, NAME):
        elements = self.driver.find_element(By.NAME, NAME)
        print("Xpath_Elements: Se interactuo con el elemento " + NAME)
        return elements
    
    def _xpath_element(self, XPATH):
        try:
            wait = WebDriverWait(self.driver, 20)
            wait.until(EC.visibility_of_element_located((By.XPATH, XPATH)))
            elements = self.driver.find_element(By.XPATH, XPATH)
            print(u"Esperar_Elemento: Se visualizo el elemento " + XPATH)
            return elements
        except TimeoutException:
            print(u"Esperar_Elemento: No presente " + XPATH)
        except TimeoutError:
            print(u"Esperar_Elemento: No presente " + XPATH)

    def _name_element(self, NAME):
        try:
            wait = WebDriverWait(self.driver, 20)
            wait.until(EC.visibility_of_element_located((By.NAME, NAME)))
            elements = self.driver.find_element(By.NAME, NAME)
            print(u"Esperar_Elemento: Se visualizo el elemento " + NAME)
            return elements
        except TimeoutException:
            print(u"Esperar_Elemento: No presente " + NAME)
        except TimeoutError:
            print(u"Esperar_Elemento: No presente " + NAME)


    ############################
    ###### LOCATORS HANDLE #####
    ############################

    def get_json_file(self, file):
        json_path = Inicializar.PAGES_DIR + "/" + file + '.json'
        try:
            with open(json_path, "r") as read_file:
                self.json_strings = json.loads(read_file.read())
                print("get_json file: "+ json_path)
                return self.json_strings
        except FileNotFoundError as e:
            self.json_strings = False
            pytest.skip(f"get_json_file: No se encontro el archivo: {e} " + file)
            Functions.tearDown(self)

    def get_entity(self, entity):
        if not self.json_strings:
            pytest.skip(f"get_entity: No se encontro el DOM para esta prueba(json string is None o false). " + entity)
        try:
            self.json_GetFieldBy = self.json_strings[entity]['GetFieldBy']
            self.json_ValueToFind = self.json_strings[entity]['ValueToFind']
            return True
        
        except KeyError as e:
            pytest.skip(f"get_entity: No se encontro la Key a la cual se hace referencia: {e} " )
            return None

############################
    ###### BEHAVIOR DRIVEN TEST #####
    ############################

    def get_elements(self, entity,  MyTextElement = None):
        Get_entity = Functions.get_entity(self, entity)

        if Get_entity is None:
            print("No se encontro el valor del Json definido")
        else:
            try:
                if self.json_GetFieldBy.lower() == "id":
                    elements = self.driver.find_element(By.ID, self.json_ValueToFind)
                if self.json_GetFieldBy.lower() == "name":
                    elements = self.driver.find_element(By.NAME, self.json_ValueToFind)
                if self.json_GetFieldBy.lower() == "xpath":
                    if MyTextElement is not None:
                        self.json_ValueToFind = self.json_ValueToFind.format(MyTextElement)
                        print(self.json_ValueToFind)
                    elements = self.driver.find_element(By.XPATH, self.json_ValueToFind)
                if self.json_GetFieldBy.lower() == "link":
                    elements = self.driver.find_element(By.PARTIAL_LINK_TEXT, self.json_ValueToFind)
                if self.json_GetFieldBy.lower() == "css":
                    elements = self.driver.find_element(By.CSS_SELECTOR, self.json_ValueToFind)
                print("Get_elements: " + self.json_ValueToFind)
                return elements
            except NoSuchElementException as e:
                print("get_text: No se encontro el elemento: {e} " + self.json_ValueToFind )
            except TimeoutException as e:
                print("get_text: No se encontro el elemento: {e} " + self.json_ValueToFind )

    def get_text(self, entity, MyTextElement = None):
        Get_entity = Functions.get_entity(self, entity)

        if Get_entity is None:
            print("No se encontro el valor del Json definido")
        else:
            try:
                if self.json_GetFieldBy.lower() == "id":
                    elements = self.driver.find_element(By.ID, self.json_ValueToFind)
                if self.json_GetFieldBy.lower() == "name":
                    elements = self.driver.find_element(By.NAME, self.json_ValueToFind)
                if self.json_GetFieldBy.lower() == "xpath":
                    if MyTextElement is not None:
                        self.json_ValueToFind = self.json_ValueToFind.format(MyTextElement)
                        print(self.json_ValueToFind)
                    elements = self.driver.find_element(By.XPATH, self.json_ValueToFind)
                if self.json_GetFieldBy.lower() == "link":
                    elements = self.driver.find_element(By.PARTIAL_LINK_TEXT, self.json_ValueToFind)
                if self.json_GetFieldBy.lower() == "css":
                    elements = self.driver.find_element(By.CSS_SELECTOR, self.json_ValueToFind)
                print("Get_text: " + self.json_ValueToFind)
                print("Get_text: " + elements.text.strip())
                return elements.text.strip()
            except NoSuchElementException as e:
                print("get_text: No se encontro el elemento: {e} " + self.json_ValueToFind )
            except TimeoutException as e:
                print("get_text: No se encontro el elemento: {e} " + self.json_ValueToFind )

    def esperar_elemento(self, locator, MyTextElement= None):
        Get_entity = Functions.get_entity(self, locator)
        if Get_entity is None:
            print("No se encontro el valor del Json definido")
        else:
            try:
                if self.json_GetFieldBy.lower() == "id":
                    wait = WebDriverWait(self.driver, 20)
                    wait.until(EC.visibility_of_element_located((By.ID, self.json_ValueToFind)))
                    wait.until(EC.element_to_be_clickable((By.ID, self.json_ValueToFind)))
                    print("Esperar_Elemento: Se visualizo el elemento " + locator)
                    return True
                if self.json_GetFieldBy.lower() == "name":
                    wait = WebDriverWait(self.driver, 20)
                    wait.until(EC.visibility_of_element_located((By.NAME, self.json_ValueToFind)))
                    wait.until(EC.element_to_be_clickable((By.NAME, self.json_ValueToFind)))
                    print("Esperar_Elemento: Se visualizo el elemento " + locator)
                    return True
                if self.json_GetFieldBy.lower() == "xpath":
                    wait = WebDriverWait(self.driver, 20)
                    if MyTextElement is not None:
                        self.json_ValueToFind = self.json_ValueToFind.format(MyTextElement)
                        print(self.json_ValueToFind)
                    wait.until(EC.visibility_of_element_located((By.XPATH, self.json_ValueToFind)))
                    wait.until(EC.element_to_be_clickable((By.XPATH, self.json_ValueToFind)))
                    print("Esperar_Elemento: Se visualizo el elemento " + locator)
                    return True
                if self.json_GetFieldBy.lower() == "link":
                    wait = WebDriverWait(self.driver, 20)
                    wait.until(EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT, self.json_ValueToFind)))
                    wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, self.json_ValueToFind)))
                    print("Esperar_Elemento: Se visualizo el elemento " + locator)
                    return True
                if self.json_GetFieldBy.lower() == "css":
                    wait = WebDriverWait(self.driver, 20)
                    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.json_ValueToFind)))
                    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.json_ValueToFind)))
                    print("Esperar_Elemento: Se visualizo el elemento " + locator)
                    return True
            except NoSuchElementException as e:
                print("get_text: No se encontro el elemento: {e} " + self.json_ValueToFind )
            except TimeoutException as e:
                print("get_text: No se encontro el elemento: {e} " + self.json_ValueToFind )

    def get_select_elements(self, entity):
            Get_entity = Functions.get_entity(self, entity)

            if Get_entity is None:
                print("No se encontro el valor del Json definido")
            else:
                try:
                    if self.json_GetFieldBy.lower() == "id":
                        select = Select(self.driver.find_element(By.ID, self.json_ValueToFind))
                    if self.json_GetFieldBy.lower() == "name":
                        select = Select(self.driver.find_element(By.NAME, self.json_ValueToFind))
                    if self.json_GetFieldBy.lower() == "xpath":
                        select = Select(self.driver.find_element(By.XPATH, self.json_ValueToFind))
                    if self.json_GetFieldBy.lower() == "link":
                        select = Select(self.driver.find_element(By.PARTIAL_LINK_TEXT, self.json_ValueToFind))
                    if self.json_GetFieldBy.lower() == "css":
                        select = Select(self.driver.find_element(By.CSS_SELECTOR, self.json_ValueToFind))
                        
                    print("Get_select_elements: " + self.json_ValueToFind)
                    return select
                except NoSuchElementException as e:
                    print("get_text: No se encontro el elemento: {e} " + self.json_ValueToFind )
                except TimeoutException as e:
                    print("get_text: No se encontro el elemento: {e} " + self.json_ValueToFind )
                    
    def select_by_text(self, entity, text):
        Functions.get_select_elements(self, entity).select_by_visible_text(text)

    def select_by_value(self, entity, text):
        Functions.get_select_elements(self, entity).select_by_value(text)

    def send_key_text(self, entity, text):
        Functions.get_elements(self, entity).send_keys(text)

    def new_windows(self, URL):
        self.driver.execute_script(f'''window.open("{URL}","_blank");''')
        Functions.page_has_loaded(self)

    def switch_to_windows_name(self, ventana):
        if ventana in self.ventanas:
            self.driver.switch_to.window(self.ventanas[ventana])
            self.driver.maximize_window()
            print(self.ventanas)
            print("Estas en " + ventana + " : " + self.ventanas[ventana])
            Functions.page_has_loaded(self)

    def new_window(self, URL):
        self.driver.execute_script(F'''window.open("{URL}","_blank");''')
        Functions.page_has_loaded(self)

    def page_has_loaded(self):
        driver = self.driver
        print("Checking if {} page is loaded.".format(self.driver.current_url))
        page_state = driver.execute_script("return document.readyState;")
        yield
        WebDriverWait(driver, 30).until(lambda driver:page_state == "complete")
        assert page_state == "complete", "No se completo la carga"

    def scroll_to(self, locator, MyTextElement=None):
        Get_Entity = Functions.get_entity(self, locator)
        if Get_Entity is None:
            return print("No se encontro el valor del json definido")
        else:
            try:
                if self.json_GetFieldBy.lower() == "id":
                    localizador = self.driver.find_element(By.ID, self.json_ValueToFind)
                    self.driver.execute_script("arguments[0].scrollIntoView()", localizador)
                    print("Scroll_to: " + locator)
                    return True
                if self.json_GetFieldBy.lower() == "xpath":
                    localizador = self.driver.find_element(By.XPATH, self.json_ValueToFind)
                    self.driver.execute_script("arguments[0].scrollIntoView()", localizador)
                    print("Scroll_to: " + locator)
                    return True
                if self.json_GetFieldBy.lower() == "link":
                    localizador = self.driver.find_element(By.PARTIAL_LINK_TEXT, self.json_ValueToFind)
                    self.driver.execute_script("arguments[0].scrollIntoView()", localizador)
                    print("Scroll_to: " + locator)
                    return True
            except TimeoutError as e:
                print(f"Scroll_to no present: {e}" + locator)

    def js_click(self, locator, MyTextElement=None):
        Get_entity = Functions.get_entity(self, locator)
        Functions.esperar_elemento(self, locator, MyTextElement)
        if Get_entity is None:
            return print("No se encontro el valor en el json definido")
        else:
            try:
                if self.json_GetFieldBy.lower() == "id":
                    localizador = self.driver.find_element(By.ID, self.json_ValueToFind)
                    self.driver.execute_script("arguments[0].click();", localizador)
                    print("Se hizo click en: " + locator)
                    return True
                if self.json_GetFieldBy.lower() == "xpath":
                    if MyTextElement is not None:
                        self.json_ValueToFind = self.json_ValueToFind.format(MyTextElement)
                        print(self.json_ValueToFind)
                    localizador = self.driver.find_element(By.XPATH, self.json_ValueToFind)
                    self.driver.execute_script("arguments[0].click();", localizador)
                    print("Se hizo click en: " + locator)
                    return True
                if self.json_GetFieldBy.lower() == "name":
                    localizador = self.driver.find_element(By.NAME, self.json_ValueToFind)
                    self.driver.execute_script("arguments[0].click();", localizador)
                    print("Se hizo click en: " + locator)
                    return True
                if self.json_GetFieldBy.lower() == "link":
                    localizador = self.driver.find_element(By.PARTIAL_LINK_TEXT, self.json_ValueToFind)
                    self.driver.execute_script("arguments[0].click();", localizador)
                    print("Se hizo click en: " + locator)
                    return True
            except TimeoutException  as e:
                print("js_click: No presente" + locator)


############################
    ###### WAIT ELEMENTS #####
    ############################
    def esperar(self, timeLoad = 10):
        print("Esperar elemento ("+str(timeLoad)+")")
        try:
            totalWait = 0
            while (totalWait < timeLoad):
                time.sleep(1)
                totalWait = totalWait + 1
                print(totalWait)
        finally:
            print("Esperar: Carga Finalizada...")
                
    def alert_windows(self, ok ="ok"):
        try:
            wait = WebDriverWait(self.driver, 30)
            wait.until(EC.alert_is_present(), print("Esperando alerta..."))
            alert = self.driver.switch_to.alert
            print(alert.text)
            if alert.lower() == "ok":
                alert.accept()
                print("Click in Accept")
            else:
                alert.dismiss()
                print("Click in Dissmiss")
        except NoAlertPresentException as e:
            print(f"Alert no presente: {e}")
        except NoSuchWindowException as e:
            print(f"Alert no presente: {e}")
        except TimeoutException as e:
            print(f"Alert no presente: {e}")

    def send_especific_key(self, element, key):
        if key.capitalize() == "Enter":
            Functions.get_elements(self, element).send_keys(Keys.ENTER)
        if key.capitalize() == "Tab":
            Functions.get_elements(self, element).send_keys(Keys.TAB)
        if key.capitalize() == "Space":
            Functions.get_elements(self, element).send_keys(Keys.SPACE)

    def assert_text(self, locator, TEXTO):
        Get_Entity = Functions.get_entity(self, locator)
        if Get_Entity is None:
            print("No se encontró el valor en el JSON definido")
            return

        locator_type = self.json_GetFieldBy.lower()
        locator_value = self.json_ValueToFind
        ObjText = None

        wait = WebDriverWait(self.driver, 20)

        if locator_type == "id":
            wait.until(EC.presence_of_element_located((By.ID, locator_value)))
            ObjText = self.driver.find_element(By.ID, locator_value).text

        elif locator_type == "xpath":
            wait.until(EC.visibility_of_element_located((By.XPATH, locator_value)))
            element = self.driver.find_element(By.XPATH, locator_value)
            ObjText = element.text
            print("[DEBUG] HTML:", element.get_attribute("outerHTML"))

        elif locator_type == "name":
            wait.until(EC.visibility_of_element_located((By.NAME, locator_value)))
            ObjText = self.driver.find_element(By.NAME, locator_value).text

        else:
            print(f"Tipo de localizador '{locator_type}' no soportado.")
            return
        
        assert TEXTO.strip() == ObjText.strip(), f"Texto no coincide:\nEsperado: {TEXTO}\nObtenido: {ObjText}"

    def check_element(self, locator):
        Get_Entity = Functions.get_entity(self, locator)
        if Get_Entity is None:
            print("No se encontró el valor en el JSON definido")
            return
        
        else:
            try:
                locator_type = self.json_GetFieldBy.lower()
                locator_value = self.json_ValueToFind
                ObjText = None

                wait = WebDriverWait(self.driver, 15)

                if locator_type == "id":
                    wait.until(EC.presence_of_element_located((By.ID, locator_value)))
                    ObjText = self.driver.find_element(By.ID, locator_value).text
                    print("check_element: Se visualizo el elemento " + locator)
                    return True

                elif locator_type == "xpath":
                    wait.until(EC.visibility_of_element_located((By.XPATH, locator_value)))
                    element = self.driver.find_element(By.XPATH, locator_value)
                    ObjText = element.text
                    print("check_element: Se visualizo el elemento " + locator)
                    return True

                elif locator_type == "name":
                    wait.until(EC.visibility_of_element_located((By.NAME, locator_value)))
                    print("check_element: Se visualizo el elemento " + locator)
                    return True

                else:
                    print(f"Tipo de localizador '{locator_type}' no soportado.")
                    return
            except NoSuchElementException as e:
                print(f"get_text(check_text): No se encontro el elemento: {e} " + locator_value)
            except TimeoutException as e:
                print(f"get_text(check_text): No se encontro el elemento: {e} " + locator_value)

############################
    ###### DATA SCENARIO #####
    ############################
    #Guarda desde un valor
    def create_variable_scenary(self, key, value):
        Scenario[key] = value
        print(Scenario)
        print("Se almaceno la key " + key + " : " + value)

    #guarda desde un elemento
    def save_variable_scenary(self, element, variable):
        Scenario[variable] = Functions.get_text(self, element)
        print(Scenario)
        print("Se almaceno el valor de " + variable + " : " + Scenario[variable])

    def get_variable_scenary(self, variable): 
        self.variable = Scenario[variable]
        print(f"get_variable_scenario: {self.variable}")
        return self.variable
        
    def compare_with_variable_scenary(self, element, variable):
        variable_scenary =  str(Scenario[variable])
        element_text = str(Functions.get_text(self, element))
        _exist = (variable_scenary in element_text)
        print(f"Comparando los valores... verificando que si {variable_scenary} esta presente en {element_text} : {_exist}")
        assert _exist == True, f'{variable_scenary} != {element_text}'

    def textDataEnviromentReplace(self, text):
        if text == "today":
            self.today = datetime.date.today()
            text = self.today.strftime(Inicializar.DateFormat)
        if text == "yesterday":
            self.today = datetime.date.today() - datetime.timedelta(days=1)
            text = self.today.strftime(Inicializar.DateFormat)
        if text == "last month":
            self.today = datetime.date.today() - datetime.timedelta(days=30)
            text = self.today.strftime(Inicializar.DateFormat)
        return text
############################
    ###### EXCEL #####
    ############################
    
    def leer_celda(self, celda):
        wb = openpyxl.load_workbook(Inicializar.Excel)
        sheet = wb["DataTest"]
        valor = str(sheet[celda].value)
        print("------------------------")
        print("El libro de excel utilizando es de es: " + Inicializar.Excel)
        print("El valor de la celda es: " + valor)
        print("------------------------")
        return valor
    
    def escribir_celda(self, celda, valor):
        wb = openpyxl.load_workbook(Inicializar.Excel)
        hoja = wb["DataTest"]
        hoja[celda] = valor
        wb.save(Inicializar.Excel)
        print("------------------------")
        print("El libro de excel utilizando es de es: " + Inicializar.Excel)
        print("Se escribio en la celda de: " + str(celda) + "el valor" + str(valor))
        print("------------------------")


############################
    ###### DATABASE #####
    ############################

    def pyodbc_conn(self, _host=None, _port=None, _dbname=None, _user=None, _pass=None):

        # Asignar valores por defecto desde Inicializar si no se pasaron
        _host = _host or Inicializar.DB_HOST
        _port = _port or Inicializar.DB_PORT
        _dbname = _dbname or Inicializar.DB_DATABASE
        _user = _user or Inicializar.DB_USER
        _pass = _pass or Inicializar.DB_PASS

        try:
            conn_str = (
                "DRIVER={MySQL ODBC 9.4 ANSI Driver};"
                f"SERVER={_host};"
                f"PORT={_port};"
                f"DATABASE={_dbname};"
                f"USER={_user};"
                f"PASSWORD={_pass};"
            )

            conn = pyodbc.connect(conn_str)
            self.cursor = conn.cursor()
            print("Connection successful.")
            return self.cursor

        except pyodbc.Error as error:
            self.conn = None
            self.cursor = None
            print("Connection failed:", error)
            # Si es para pruebas, lanza una excepción controlada o re-raise
            raise RuntimeError("Error al conectar a la base de datos: " + str(error))
    
    def pyodbc_query(self, _query):
        self.cursor = Functions.pyodbc_conn(self)
        if self.cursor is not None:
            try:
                self.cursor.execute(_query)
                self.Result = self.cursor.fetchall()
                for row in self.Result:
                    print(row)
            except (pyodbc.Error) as error:
                print("Error en la consulta", error)
            finally:
                if (self.cursor):
                    self.cursor.close()
                    print("pyodbc Se cerro la conexion")

############################
    ###### SCREENSHOTS #####
    ############################
    def create_path(self):
        day = time.strftime("%Y-%m-%d")
        hour_act = time.strftime("%H%M%S")

        general_path = Inicializar.path_evidencias
        driver_test = Inicializar.NAVEGADOR
        test_case = self.__class__.__name__
        
         # Verifica si "context" está en el nombre de la clase del test
        if "context" in test_case.lower():
            path = f"{general_path}/{day}/{driver_test}/{hour_act}/"
        else:
            path = f"{general_path}/{day}/{test_case}/{driver_test}/{hour_act}/"

        # Crea el directorio si no existe
        os.makedirs(path, exist_ok=True)
        return path
    
    def captura_pantalla(self):
        try:
            path = self.create_path()
            test_case = self.__class__.__name__
            hour_act = time.strftime("%H%M%S")
            img_path = os.path.join(path, f"{test_case}_{hour_act}.png")
            self.driver.get_screenshot_as_file(img_path)
            
            print(f"Captura guardada en: {img_path}")  # Usa logging si es producción
            return img_path
        
        except Exception as e:
            print(f"Error al capturar pantalla: {e}")
        return None
    
    def create_path_behave(context):
        general_path = Inicializar.path_evidencias
        driver_test = Inicializar.NAVEGADOR
        day = time.strftime("%Y-%m-%d")
        hour_act = time.strftime("%H%M%S")
        test_case="behave"

        if "context" in test_case.lower():
            path = f"{general_path}/{day}/{driver_test}/{hour_act}/"
        else:
            path = f"{general_path}/{day}/{test_case}/{driver_test}/{hour_act}/"

        # Crea el directorio si no existe
        os.makedirs(path, exist_ok=True)
        return path
    
    def captura_pantalla_behave(context):
        try:
            path = Functions.create_path_behave(context)
            hour_act = time.strftime("%H%M%S")
            img_path = os.path.join(path, f"captura_{hour_act}.png")
            context.driver.get_screenshot_as_file(img_path)
            
            print(f"Captura guardada en: {img_path}")  # Usa logging si es producción
            return img_path
        
        except Exception as e:
            print(f"Error al capturar pantalla: {e}")
        return None

    def captura(self, Description):
        allure.attach(self.driver.get_screenshot_as_png(), Description, attachment_type=allure.attachment_type.PNG)

    def validar_elemento(self, locator):
        get_entity = Functions.get_entity(self, locator)
        
        time_out = 10
        if get_entity is None:
            return print("No se encontro el valor en el json definido")
        else:
            try:
                if self.json_GetFieldBy.lower() == "id":
                    wait = WebDriverWait(self.driver, time_out)
                    wait.until(EC.visibility_of_element_located((By.ID, self.json_ValueToFind)))
                    wait.until(EC.element_to_be_clickable((By.ID, self.json_ValueToFind)))
                    print("Esperar_elemento: Se visualizo el elemento " + locator)
                    return True
                if self.json_GetFieldBy.lower() == "name":
                    wait = WebDriverWait(self.driver, time_out)
                    wait.until(EC.visibility_of_element_located((By.NAME, self.json_ValueToFind)))
                    wait.until(EC.element_to_be_clickable((By.NAME, self.json_ValueToFind)))
                    print("Esperar_elemento: Se visualizo el elemento " + locator)
                    return True
                if self.json_GetFieldBy.lower() == "xpath":
                    wait = WebDriverWait(self.driver, time_out)
                    wait.until(EC.visibility_of_element_located((By.XPATH, self.json_ValueToFind)))
                    wait.until(EC.element_to_be_clickable((By.XPATH, self.json_ValueToFind)))
                    print("Esperar_elemento: Se visualizo el elemento " + locator)
                    return True
                if self.json_GetFieldBy.lower() == "link":
                    wait = WebDriverWait(self.driver, time_out)
                    wait.until(EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT, self.json_ValueToFind)))
                    wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, self.json_ValueToFind)))
                    print("Esperar_elemento: Se visualizo el elemento " + locator)
                    return True
            except TimeoutException:
                print("Assert path: Elemento no presente " + locator)
                return False
    
    def replace_with_context_values(self, text):
        pattern = r"Scenario:(\w+)"
        matches = re.findall(pattern, text, re.IGNORECASE)

        for variable in matches:
            if variable.lower() == "today":
                replacement = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
            else:
                replacement = Inicializar.Scenario.get(variable)
                if replacement is None:
                    continue  # o puedes lanzar un error si es crítico
            text = re.sub(f"Scenario:{variable}", replacement, text, flags=re.IGNORECASE)
        print(text)
        return text


    