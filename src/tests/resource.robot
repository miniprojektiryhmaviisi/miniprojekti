*** Settings ***
Library  ../ReferencesLibrary.py

*** Keywords ***
Input Add Reference Command
    Input    "0"

Input Book Command
    Input    a

Input Article Command
    Input    b

Input Inproceedings Command
    Input    c


Book Input Credentials
    [Arguments]
    ...    ${key}
    ...    ${author}
    ...    ${space}
    ...    ${title}
    ...    ${year}
    ...    ${publisher}
    ...    ${volume}
    ...    ${number}
    ...    ${pages}
    ...    ${month}
    ...    ${note}
    Input    ${key}
    Input    ${author}
    Input    ${space}
    Input    ${title}
    Input    ${year}
    Input    ${publisher}
    Input    ${volume}
    Input    ${number}
    Input    ${pages}
    Input    ${month}
    Input    ${note}
