*** Settings ***
Resource       resource.robot
Suite Setup    Prepare DB

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
    Input Search Command
    Input Both Search Details
    ...    Book Author
    ...    Book Title
    Input Exit Command
    Execute App
    Output Should Contain  Cite Key${SPACE*5}: TestKey1

Search Existing Article Reference Both   
    Input Search Command
    Input Both Search Details
    ...    Article Author
    ...    Article Title
    Input Exit Command
    Execute App
    Output Should Contain  Cite Key${SPACE*5}: TestKey2

Search Existing Inproceedings Reference Both
    Input Search Command
    Input Both Search Details
    ...    Inproceedings Author
    ...    Inproceedings Title
    Input Exit Command
    Execute App
    Output Should Contain  Cite Key${SPACE*5}: TestKey3


*** Keywords ***
Prepare DB
    Input Delete Command
    Input Delete Confirmation
    Input Add Reference Command
    Input Book Command
    Book Input Details
    ...    TestKey1
    ...    Book Title
    ...    Book Author
    ...    MacMillan
    ...    1991
    ...    682
    ...    1
    ...    100-108
    ...    12
    ...    ${EMPTY}
    Input Add Reference Command
    Input Article Command
    Article Input Details
    ...    TestKey2
    ...    Article Title
    ...    Article Author
    ...    MacMillan
    ...    1991
    ...    682
    ...    1
    ...    100-108
    ...    12
    ...    ${EMPTY}
    Input Add Reference Command
    Input Inproceedings Command
    Inproceedings Input Details
    ...    TestKey3
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