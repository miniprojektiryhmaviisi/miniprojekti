*** Settings ***
Resource      resource.robot
Test Setup    Prepare DB   

*** Test Cases ***
<<<<<<< HEAD
List all references
    Input View Command
    Input Exit Command
    Execute App
    Output Should Contain    ---------------
    Output Should Contain    Book references
    Output Should Contain    ---------------
    Output Should Contain    Cite Key\ \ \ \ \ : TestKey
    Output Should Contain    Author\ \ \ \ \ \ \ : Stallings
    Output Should Contain    Title\ \ \ \ \ \ \ \ : Operating Systems
    Output Should Contain    Publisher\ \ \ \ : MacMillan
    Output Should Contain    Year\ \ \ \ \ \ \ \ \ : 1991
    Output Should Contain    Volume\ \ \ \ \ \ \ : 682
    Output Should Contain    Number\ \ \ \ \ \ \ : 1
    Output Should Contain    Pages\ \ \ \ \ \ \ \ : 100-108
    Output Should Contain    Month\ \ \ \ \ \ \ \ : 12
    Output Should Contain    ---------------

*** Keywords ***
Prepare DB
    Input Delete Command
    Input Delete Confirmation
    Input Add Reference Command
=======
List all book references
    ${key}=    Get Time    epoch
    Log    Generated key: ${key}
>>>>>>> c323ac8 (listing robot)
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
<<<<<<< HEAD
=======
    Input View Command
    Input Exit Command
    Ask Form
    Output Should Contain    ---------------
    Output Should Contain    Book references
    Output Should Contain    ---------------\n

List all article references
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
    Input View Command
    Input Exit Command
    Ask Form
    Output Should Contain    ---------------
    Output Should Contain    Article references
    Output Should Contain    ---------------\n

List all inproceedings references
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
    Input View Command
    Input Exit Command
    Ask Form
    Output Should Contain    ---------------
    Output Should Contain    Inproceedings references
    Output Should Contain    ---------------\n
>>>>>>> c323ac8 (listing robot)
