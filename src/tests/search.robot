*** Settings ***
Resource        resource.robot

*** Test Cases  ***
Search Nonexistent Reference Both
    Input Search Command
    Input Both Search Details
    ...    No one
    ...    Blank
    Input Exit Command
    Execute App
    Output Should Contain  No references found!

Search Existing Book Reference Both
    Input Add Reference Command
    ${key}=    Get Time    epoch
    Log    Generated key: ${key}
    Input Book Command
    Book Input Details
    ...    ${key}
    ...    Book Title
    ...    Book Author
    ...    MacMillan
    ...    1991
    ...    682
    ...    1
    ...    100-108
    ...    12
    ...    ${EMPTY}
    Input Search Command
    Input Both Search Details
    ...    Book Author
    ...    Book Title
    Input Exit Command
    Execute App
    Output Should Contain  Cite Key${SPACE*5}: ${key}

Search Existing Article Reference Both
    Input Add Reference Command
    ${key}=    Get Time    epoch
    Log    Generated key: ${key}
    Input Article Command
    Article Input Details
    ...    ${key}
    ...    Article Title
    ...    Article Author
    ...    MacMillan
    ...    1991
    ...    682
    ...    1
    ...    100-108
    ...    12
    ...    ${EMPTY}
    Input Search Command
    Input Both Search Details
    ...    Article Author
    ...    Article Title
    Input Exit Command
    Execute App
    Output Should Contain  Cite Key${SPACE*5}: ${key}

Search Existing Inproceedings Reference Both
    Input Add Reference Command
    ${key}=    Get Time    epoch
    Log    Generated key: ${key}
    Input Inproceedings Command
    Inproceedings Input Details
    ...    ${key}
    ...    Inproceedings Title
    ...    Inproceedings Author
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
    Input Search Command
    Input Both Search Details
    ...    Inproceedings Author
    ...    Inproceedings Title
    Input Exit Command
    Execute App
    Output Should Contain  Cite Key${SPACE*5}: ${key}
