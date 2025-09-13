*** Settings ***
Documentation    Paylocity
Library    SeleniumLibrary
Library    OperatingSystem
Library    String
Resource   ../keywords/keyword_13.robot

Suite Setup    Start
Suite Teardown    End

*** Variables ***
${url} =    https://wmxrwq14uc.execute-api.us-east-1.amazonaws.com/Prod/Account/Login
${browser} =    chrome
${user} =    TestUser803
${password} =    ;PX7m}9t}TVZ
${FIRST_NAME} =    Juan
${LAST_NAME} =    Lopez
${DEPENDENTS} =    2
*** Test Cases ***
Test Case 1: Login
    [Documentation]    Validate the user login wih the right credentials
    [Tags]    Login
    Input Text    name=Username    ${user}
    Input Text    id=Password    ${Password}
    Click Button    //button[normalize-space()='Log In']
    F_screenshot_allure    login_success
Tests case 2: Add empployee
    [Documentation]    Validate the user can add a new employee
    [Tags]    add_employee

    Input Text    name=Username    ${user}
    Input Text    id=Password    ${Password}
    Click Button    //button[normalize-space()='Log In']
    
    Wait Until Element Is Visible    id=add
    Click Button    id=add
    Wait Until Element Is Enabled    name=firstName
    Input Text    name=firstName    Liliana
    Input Text    name=lastName    Zamora
    Input Text    name=dependants    1
    Click Button    id=addEmployee
    Sleep    4
    F_screenshot    Add_employee

Tests case 3: Edit employee: Name Field
    [Documentation]    Validate the user can edit an employee
    [Tags]    edit_name
    Input Text    name=Username    ${user}
    Input Text    id=Password    ${Password}
    Click Button    //button[normalize-space()='Log In']
    Click Element    xpath=//i[@class='fas fa-edit']
    Wait Until Element Is Visible    name=firstName
    Clear Element Text    name=firstName
    Input Text    name=firstName    ${FIRST_NAME}
    Clear Element Text    name=lastName
    Input Text    name=lastName    Velencia
    Clear Element Text    name=dependants
    Input Text    name=dependants    1
    Click Button    id=updateEmployee
    Sleep    6
    Wait Until Element Is Visible    xpath=//table[@id='employeesTable']//td[normalize-space()='${FIRST_NAME}']
    Element Text Should Be           xpath=//table[@id='employeesTable']//td[normalize-space()='${FIRST_NAME}']    ${FIRST_NAME}
    F_screen_element     xpath=//table[@id='employeesTable']//td[normalize-space()='${FIRST_NAME}']    edit_name


Tests case 4: Delete Employee
    [Documentation]    Validate the user can edit an employee
    [Tags]    rm_employee
    Input Text    name=Username   ${user}
    Input Text    id=Password    ${Password}
    Click Button    //button[normalize-space()='Log In']
    
    Click Element    xpath=//i[@class='fas fa-times']
    Element Should Contain    xpath=//h5[normalize-space()='Delete Employee']    Delete Employee
    Element Should Contain    xpath=//div[@class='col-sm-12']    Delete employee record for
    Element Should Contain    xpath=//button[@id='deleteEmployee']    Delete
    Click Element    xpath=//button[@id='deleteEmployee']
    Sleep    10
    Element Should Not Be Visible    xpath=//i[@class='fas fa-edit']
    F_screenshot    remove_employee

*** Keywords ***
Start
    [Documentation]
    [Tags]
    Log    QA: ${name} ${last_name}
    Open Browser    ${url}    ${browser}   
    Maximize Browser Window
    Set Selenium Speed    .1s
    Set Selenium Implicit Wait    20
    Title Should Be    Log In - Paylocity Benefits Dashboard

End
    Sleep    2
    Close Browser   