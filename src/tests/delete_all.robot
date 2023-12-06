*** Settings ***
Resource        resource.robot
Test Setup    Prepare DB

*** Test Cases ***
Export all references
    Input Delete Command
    Input    delete
    Input View Command
    Input Exit Command
    Execute App
    Output Should Contain    No references

*** Keywords ***
Prepare DB
    Input Add Reference Command
    Input Book Command
    Book Input Details
    ...    TestKey
    ...    Operating Systems
    ...    Stallings
    ...    MacMillan
    ...    1991
    ...    682
    ...    1
    ...    100-108
    ...    12
    ...    ${EMPTY}
    