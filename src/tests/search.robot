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
