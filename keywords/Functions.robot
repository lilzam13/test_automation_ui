*** Settings ***
Library    SeleniumLibrary
##Library    Dialogs
Library     AllureLibrary
Library     RequestsLibrary
*** Variables ***
${screen_path} =    C:/Users/lilia/Desktop/python-robot/src/data/capturas/allure/
${url1} =    https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
*** Keywords ***
Abrir Navegador Seguro
    [Arguments]    ${url1}
    ${chrome_options}=    Set Variable    --no-sandbox,--disable-dev-shm-usage,--disable-gpu,--headless=new,--user-data-dir=/tmp/robot-profile-${TEST NAME}
    Open Browser    ${url1}    chrome    options=${chrome_options}
    Maximize Browser Window
    Set Selenium Speed    .1s
    Set Selenium Implicit Wait    50

F_texto
    [Arguments]    ${sel}    ${dato}
    Wait Until Element Is Visible    ${sel}    
    Wait Until Element Is Enabled    ${sel}
    Element Should Be Visible    ${sel}
    Clear Element Text    ${sel}
    #Execute Javascript    window.scrollTo(0,20)
    input text    ${sel}    ${dato}
    #Capture Element Screenshot    ${sel}    ${screen_path}${dato}.png
    RETURN    La captura fue correcta
    
F_enter
    [Arguments]    ${sel}
    Wait Until Element Is Visible    ${sel}    
    Wait Until Element Is Enabled    ${sel}
    Element Should Be Visible    ${sel}
    Press Keys    xpath=//*[@id="APjFqb"]    ENTER 

F_screenshot
    [Arguments]    ${name_img}
    ${capture_path}=    Set Variable    ${OUTPUT DIR}/${name_img}
    Capture Page Screenshot    ${capture_path}

F_screenshot_allure
    [Arguments]    ${name_img}   
    ${screenshot_path}=    Capture Page Screenshot    ${OUTPUT DIR}/${name_img}
    Attach File    ${screenshot_path}

F_screen_element
    [Arguments]    ${sel}    ${name_img}
    Wait Until Element Is Visible    ${sel}    
    Wait Until Element Is Enabled    ${sel}
    Element Should Be Visible    ${sel}
    Capture Element Screenshot    ${sel}    ${screen_path}${name_img}

F_scroll
    [Documentation]    Sirve para realizar un scroll en la pagina
    [Arguments]    ${x}    ${y}
    Execute Javascript    window.scrollTo(${x},${y})

F_click_xy
    [Documentation]    Hacer click de acuerdo a cordenadas
    [Arguments]    ${sel}    ${x}    ${y}
    Click Element At Coordinates    ${sel}    ${x}    ${y}

F_pedir_valor
    [Documentation]    Hacer click de acuerdo a cordenadas
    [Arguments]    ${texto}
    ${valor}=    Get Value From User    ${texto}    
    RETURN    ${valor}

   
    