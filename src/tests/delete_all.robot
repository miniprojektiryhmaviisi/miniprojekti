*** Settings ***
Resource        resource.robot

*** Test Cases ***
Export all references
    Input Delete Command
    Input    delete
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
    Input Bibtex Command
    Input Exit Command
    Ask Form
    Parse And Check Bibfile