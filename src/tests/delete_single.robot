*** Settings ***
Resource      resource.robot

*** Test Cases ***
Delete Single Reference
    Prepare Book Reference
    Input Single Reference Deletion Command
    Input Book Key
    ...    TestKey1
    Input View Command
    Input Exit Command
    Execute App
    Output Should Contain    No references

Delete Multiple References
    Prepare DB
    Input Single Reference Deletion Command
    Input All Keys
    ...    TestKey1
    ...    TestKey2
    ...    TestKey3
    Input View Command
    Input Exit Command
    Execute App
    Output Should Contain    No references

Delete Reference With Wrong Key
    Prepare Book Reference
    Input Single Reference Deletion Command
    Input Book Key
    ...    wrongkey
    Input View Command
    Input Exit Command
    Execute App
    Output Should Contain    Reference(s) with cite key(s)\n ----\ndeleted.

*** Keywords ***
Prepare Book Reference
    Input Delete Command
    Input Delete Confirmation
    Input Add Reference Command
    Input Book Command
    Book Input Details
    ...    TestKey1
    ...    Operating Systems
    ...    Stallings
    ...    MacMillan
    ...    1991
    ...    682
    ...    1
    ...    100-108
    ...    12
    ...    ${EMPTY}
    