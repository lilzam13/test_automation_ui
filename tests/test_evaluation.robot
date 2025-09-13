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
${gross_pay} =    2000
${employed_cost_year} =    1000
${employee_cost_dependent} =    500
${pay_period} =    26
*** Test Cases ***
Tests case 1: Add user: 1 dependant
    [Documentation]    Validate the user can add a new employee
    [Tags]    add_employee
    
    ${dependents}=    Set Variable    2
    ${expected_benefits}=    Benefit cost    ${dependents}
    ${expected_net}=    Next pay employee   ${expected_benefits}

    Input Text    name=Username    ${user}
    Input Text    id=Password    ${Password}
    Click Button    //button[normalize-space()='Log In']
    
    Wait Until Element Is Visible    id=add
    Click Button    id=add
    Wait Until Element Is Enabled    name=firstName
    Input Text    name=firstName    Liliana
    Input Text    name=lastName    Zamora
    Input Text    name=dependants    ${dependents}
    Click Button    id=addEmployee
    ${row}=    Get Text    //table/tbody/tr[last()]
    Should Contain    ${row}    ${expected_benefits}
    Should Contain    ${row}    ${expected_net}

Tests case 0: Add user: 0 dependant
    [Documentation]    Validate the user can add a new employee
    [Tags]    no_dependent
    
    ${dependents}=    Set Variable    0
    ${expected_benefits}=    Benefit cost    ${dependents}
    ${expected_net}=    Next pay employee   ${expected_benefits}

    Input Text    name=Username    ${user}
    Input Text    id=Password    ${Password}
    Click Button    //button[normalize-space()='Log In']
    
    Wait Until Element Is Visible    id=add
    Click Button    id=add
    Wait Until Element Is Enabled    name=firstName
    Input Text    name=firstName    Liliana
    Input Text    name=lastName    Zamora
    Input Text    name=dependants    ${dependents}
    Click Button    id=addEmployee
    ${row}=    Get Text    //table/tbody/tr[last()]
    Should Contain    ${row}    ${expected_benefits}
    Should Contain    ${row}    ${expected_net}
    
Tests case 3: Update user: 1 dependant
    [Documentation]    Validate the user can add a new employee
    [Tags]    edit_uno_dependent
    
    ${dependents}=    Set Variable    2
    ${expected_benefits}=    Benefit cost    ${dependents}
    ${expected_net}=    Next pay employee   ${expected_benefits}

    Input Text    name=Username    ${user}
    Input Text    id=Password    ${Password}
    Click Button    //button[normalize-space()='Log In']
    
    Click Element    xpath=//i[@class='fas fa-edit']
    Input Text    name=dependants    ${dependents}
    Click Button    id=updateEmployee

    ${row}=    Get Text    //table/tbody/tr[last()]
    Should Contain    ${row}    ${expected_benefits}
    Should Contain    ${row}    ${expected_net}

Tests case 0: Update user: 0 dependant
    [Documentation]    Validate the user can add a new employee
    [Tags]    edit_no_dependent
    
    ${dependents}=    Set Variable    0
    ${expected_benefits}=    Benefit cost    ${dependents}
    ${expected_net}=    Next pay employee   ${expected_benefits}

    Input Text    name=Username    ${user}
    Input Text    id=Password    ${Password}
    Click Button    //button[normalize-space()='Log In']
    
    Click Element    xpath=//i[@class='fas fa-edit']
    Input Text    name=dependants    ${dependents}
    Click Button    id=updateEmployee
    ${row}=    Get Text    //table/tbody/tr[last()]
    Should Contain    ${row}    ${expected_benefits}
    Should Contain    ${row}    ${expected_net}

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

Benefit cost
    [Arguments]    ${dependents}
    ${totalCostEmployee}=    Evaluate    round((float(${employed_cost_year}) + (float(${employee_cost_dependent}) * float(${dependents}))) / float(${pay_period}), 2)
    ${totalCostEmployee}=    Convert To String    ${totalCostEmployee}
    [Return]    ${totalCostEmployee}

Next pay employee
    [Arguments]    ${totalCostEmployee}
    ${totalToPay}=    Evaluate    round(float(${gross_pay}) - float(${totalCostEmployee}), 2)
    ${totalToPay}=    Convert To String    ${totalToPay}
    [Return]    ${totalToPay}
