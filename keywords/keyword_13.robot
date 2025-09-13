*** Settings ***
Documentation    Creando Keywords desde Python
Library    SeleniumLibrary
Resource   ../keywords/Functions.robot


*** Variables ***
${name} =    Pedro
${last_name} =    Lopez
${url} =    https://petstore.octoperf.com/actions/Account.action?newAccountForm=
${browser} =    chrome


*** Keywords ***
Cargar el navegador
    [Documentation]    Usar las funciones e interactuar con los elementos
    [Tags]     Practica 1
    Log    QA: ${name} ${last_name}
    Open Browser    ${url}    ${browser}   
    Maximize Browser Window
    Set Selenium Speed    .1s
    Set Selenium Implicit Wait    50
    Title Should Be    JPetStore Demo

Validar labels
    Wait Until Element Contains     //h3[normalize-space()='User Information']   User Information
    Wait Until Element Contains     //h3[normalize-space()='Account Information']   Account Information
    Wait Until Element Contains     //h3[normalize-space()='Profile Information']   Profile Information
    Wait Until Page Contains Element    //*[@id="CTA"]

Capturar informacion del usuario
    [Arguments]    ${user_name}    ${user_pass}    ${user_repete_pass}
    F_texto    name=username    ${user_name}
    F_texto    name=password    ${user_pass}
    F_texto    name=repeatedPassword    ${user_repete_pass}

Capturar informacion general de la cuenta
    [Arguments]    ${ac_name}    ${ac_lastname}    ${ac_email}    ${ac_phone}    
    Element Should Be Visible   //input[@name='account.firstName']
    F_texto    //input[@name='account.firstName']    ${ac_name}
    F_texto    //input[@name='account.lastName']    ${ac_lastname}
    F_texto    name=account.email    ${ac_email}
    F_texto    name=account.phone    ${ac_phone}
Capturar direccion de la cuenta
    [Arguments]    ${ac_street1}    ${ac_street2}    ${ac_city}    ${ac_state}    ${ac_zip}    ${ac_country}
    F_texto    name=account.address1    ${ac_street1}
    F_texto    name=account.address2    ${ac_street2}
    F_texto    name=account.city    ${ac_city}
    F_texto    name=account.state    ${ac_state}
    F_texto    name=account.zip    ${ac_zip}
    F_texto    name=account.country    ${ac_country}

Selecionar preferencias
    [Arguments]    ${ac_language}    ${ac_category}
    Element Should Be Enabled   //select[@name='account.languagePreference'] 
    Select From List By Value    //select[@name='account.languagePreference']    ${ac_language}
    Select From List By Value    //select[@name='account.favouriteCategoryId']    ${ac_category}
    Execute Javascript    window.scrollTo(0,100)

Afirmar configuracion adicional
    Select Checkbox    //input[@name='account.listOption']
    Select Checkbox    //input[@name='account.bannerOption']
    Click Button    //input[@name='newAccount']

Finalizar ejecucion
    Sleep    2
    Close Browser

