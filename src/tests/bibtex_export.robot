*** Settings ***
Resource        resource.robot
Test Setup    Prepare DB

*** Test Cases ***
Export all references
    Input Bibtex Command
    Input Exit Command
    Execute App
    Parse And Check Bibfile


*** Keywords ***
Prepare DB
    Input Delete Command
    Input Delete Confirmation
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