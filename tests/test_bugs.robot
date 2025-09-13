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
${EMPTY}=    Set Variable    ${EMPTY}

*** Test Cases ***
Tests case 1: Add employee: Dependent(characters)
    [Documentation]    Dependent value should not be characters
    [Tags]    characters

    Input Text    name=Username    ${user}
    Input Text    id=Password    ${Password}
    Click Button    //button[normalize-space()='Log In']
    
    Wait Until Element Is Visible    id=add
    Click Button    id=add    
    Wait Until Element Is Enabled    name=firstName
    Input Text    name=firstName    Liliana
    Input Text    name=lastName    Zamora
    Input Text    name=dependants    ab
    Click Button    id=addEmployee
    Element Should Not Be Visible    xpath=//*[@id="employeeModal"]/div/div/div[1]/h5

Tests case 2: Add employee: Dependent(negative value)
    [Documentation]    Dependent value should not be negative
    [Tags]    negative

    Input Text    name=Username    ${user}
    Input Text    id=Password    ${Password}
    Click Button    //button[normalize-space()='Log In']
    
    Wait Until Element Is Visible    id=add
    Click Button    id=add    
    Wait Until Element Is Enabled    name=firstName
    Input Text    name=firstName    Liliana
    Input Text    name=lastName    Zamora
    Input Text    name=dependants    -1
    Click Button    id=addEmployee
    Element Should Contain    xpath=//div[@id='employeeModal']//div[@class='modal-footer']    "The field Dependants must be between 0 and 32."

Tests case 3: Add employee: Dependent(maximum value)
    [Documentation]    Dependent value should not be more than 32
    [Tags]    negative

    Input Text    name=Username    ${user}
    Input Text    id=Password    ${Password}
    Click Button    //button[normalize-space()='Log In']
    
    Wait Until Element Is Visible    id=add
    Click Button    id=add    
    Wait Until Element Is Enabled    name=firstName
    Input Text    name=firstName    Liliana
    Input Text    name=lastName    Zamora
    Input Text    name=dependants    33
    Click Button    id=addEmployee
    Element Should Contain    xpath=//div[@id='employeeModal']//div[@class='modal-footer']    "The field Dependants must be between 0 and 32."

Tests case 3: Add employee: Dependent(float type)
    [Documentation]    Dependent value should not be float type
    [Tags]    float

    Input Text    name=Username    ${user}
    Input Text    id=Password    ${Password}
    Click Button    //button[normalize-space()='Log In']
    
    Wait Until Element Is Visible    id=add
    Click Button    id=add    
    Wait Until Element Is Enabled    name=firstName
    Input Text    name=firstName    Liliana
    Input Text    name=lastName    Zamora
    Input Text    name=dependants    12.32
    Click Button    id=addEmployee
    Element Should Not Be Visible    xpath=//*[@id="employeeModal"]/div/div/div[1]/h5

Tests case 4: Add employee: First Name(Maximum number)
    [Documentation]    Name value should be not more than 50
    [Tags]    Max_name

    Input Text    name=Username    ${user}
    Input Text    id=Password    ${Password}
    Click Button    //button[normalize-space()='Log In']
    
    Wait Until Element Is Visible    id=add
    Click Button    id=add    
    Wait Until Element Is Enabled    name=firstName
    Input Text    name=firstName    asdahsuidfiasdfpoiasudfoiausdfiouasiodfuasoidfuoasi
    Input Text    name=lastName    Zamora
    Input Text    name=dependants    1
    Click Button    id=addEmployee
    Element Should Contain    xpath=//div[@id='employeeModal']//div[@class='modal-footer']    "The field FirstName must be a string with a maximum length of 50."

Tests case 5: Add employee: Last name (Maximum number)
    [Documentation]    Last name value should be not more than 50
    [Tags]    max_name
    Input Text    name=Username    ${user}
    Input Text    id=Password    ${Password}
    Click Button    //button[normalize-space()='Log In']
    
    Wait Until Element Is Visible    id=add
    Click Button    id=add    
    Wait Until Element Is Enabled    name=firstName
    Input Text    name=firstName    Liliana
    Input Text    name=lastName    asdahsuidfiasdfpoiasudfoiausdfiouasiodfuasoidfuoasi
    Input Text    name=dependants    1
    Click Button    id=addEmployee
    Element Should Contain    xpath=//div[@id='employeeModal']//div[@class='modal-footer']    "The field LastName must be a string with a maximum length of 50."

Tests case 6: Add employee: First Name is required
    [Documentation]    First name should be required
    [Tags]    name_required
    
    Input Text    name=Username    ${user}
    Input Text    id=Password    ${Password}
    Click Button    //button[normalize-space()='Log In']
    
    Wait Until Element Is Visible    id=add
    Click Button    id=add    
    Wait Until Element Is Enabled    name=firstName
    Input Text    name=firstName    ${EMPTY}
    Input Text    name=lastName    Zamora
    Input Text    name=dependants    1
    Click Button    id=addEmployee
    Element Should Contain    xpath=//div[@id='employeeModal']//div[@class='modal-footer']    The FirstName field is required.

Tests case 6: Add employee: lastname is required
    [Documentation]    Last name should be required
    [Tags]    last_required
    
    Input Text    name=Username    ${user}
    Input Text    id=Password    ${Password}
    Click Button    //button[normalize-space()='Log In']
    
    Wait Until Element Is Visible    id=add
    Click Button    id=add    
    Wait Until Element Is Enabled    name=firstName
    Input Text    name=firstName    Perla
    Input Text    name=lastName    ${EMPTY}   
    Input Text    name=dependants    1
    Click Button    id=addEmployee
    Element Should Contain    xpath=//div[@id='employeeModal']//div[@class='modal-footer']    The LastName field is required.

Tests case 6: Add employee: Dependents is required
    [Documentation]    Dependents should be required
    [Tags]    depend_required
    
    Input Text    name=Username    ${user}
    Input Text    id=Password    ${Password}
    Click Button    //button[normalize-space()='Log In']
    
    Wait Until Element Is Visible    id=add
    Click Button    id=add    
    Wait Until Element Is Enabled    name=firstName
    Input Text    name=firstName    Perla
    Input Text    name=lastName    ${EMPTY} 
    Input Text    name=dependants    1Dependents
    Click Button    id=addEmployee
    Element Should Contain    xpath=//div[@id='employeeModal']//div[@class='modal-footer']    The Dependents field is required.


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