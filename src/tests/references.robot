*** Settings ***
Resource        resource.robot
Test Setup      Input Add Reference Command


*** Test Cases ***
Add Book Reference With Valid Input
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
    Input Exit Command
    Execute App
    Output Should Contain    New reference added!

Add Article Reference With Valid Input
    ${key}=    Get Time    epoch
    Log    Generated key: ${key}
    Input Article Command
    Article Input Details
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
    Input Exit Command
    Execute App
    Output Should Contain    New reference added!

Add Inproceedings Reference With Valid Input
    ${key}=    Get Time    epoch
    Log    Generated key: ${key}
    Input Inproceedings Command
    Inproceedings Input Details
    ...    ${key}
    ...    Operating Systems
    ...    Stallings
    ...    MacMillan
    ...    Booktitle1
    ...    1991
    ...    editor1
    ...    682
    ...    1
    ...    6
    ...    100-108
    ...    address
    ...    12
    ...    org1
    ...    note1
    Input Exit Command
    Execute App
    Output Should Contain    New reference added!

Add Empty Reference For Non-Optional Fields
    ${key}=    Get Time    epoch
    Log    Generated key: ${key}
    Input Book Command
    Book Input Details Mandatory Empty
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
    Input Exit Command
    Execute App
    Output Should Contain    Field cannot be empty. Please provide a valid input.

Add Book Reference with already used cite key
    ${key}=    Get Random Key
    ${key2}=    Get Random Key
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
   Input Add Reference Command
   Input Book Command
   Book Input Details Two Keys
   ...    ${key}
   ...    ${key2}
   ...    Operating Systems
   ...    Stallings
   ...    MacMillan
   ...    1991
   ...    682
   ...    1
   ...    100-108
   ...    12
   ...    ${EMPTY}
   Input Exit Command
   Execute App
   Output Should Contain    Failed to save new reference: UNIQUE constraint failed: BReferences.dbkey
