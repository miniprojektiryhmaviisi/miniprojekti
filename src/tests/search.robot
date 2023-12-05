*** Settings ***
Resource        resource.robot

*** Test Cases  ***
Search Nonexistent Reference Both
    Input Search Command
    Input Both Search Details
    ...    No one
    ...    Blank
    Input Exit Command
    Ask Form
    Output Should Contain  No references found!

Search Existing Book Reference Both
    Add Book Reference
    Input Search Command
    Input Both Search Details
    ...    Book Author
    ...    Book Title
    Input Exit Command
    Ask Form
    Output Should Contain  Book references

Search Existing Article Reference Both
    Add Article Reference
    Input Search Command
    Input Both Search Details
    ...    Article Author
    ...    Article Title
    Input Exit Command
    Ask Form
    Output Should Contain  Article references

Search Existing Inproceedings Reference Both
    Add Inproceedings Reference
    Input Search Command
    Input Both Search Details
    ...    Inproceedings Author
    ...    Inproceedings Title
    Input Exit Command
    Ask Form
    Output Should Contain  Inproceedings references

*** Keywords ***
Add Book Reference
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

Add Article Reference
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

Add Inproceedings Reference
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