*** Settings ***
Resource        resource.robot

Test Setup      Input Add Reference Command


*** Test Cases ***
List all references
    ${key}=    Get Time    epoch
    Log    Generated key: ${key}
    Input Book Command
    Book Input Details
    ...    ${key}
    ...    Operating Systems
    ...    Stallings
    ...    MacMillan
    ...    1991
    ...    682
    ...    1
    ...    100-108
    ...    12
    ...    ${EMPTY}
    Input View Command
    Input Exit Command
    Execute App
    Output Should Contain    ---------------
    Output Should Contain    Book references
    Output Should Contain    ---------------\n
