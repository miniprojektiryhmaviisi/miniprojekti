*** Settings ***
Library  references_library.ReferencesLibrary

*** Keywords ***
Input Add Reference Command
    Input    0

Input Book Command
    Input    A

Input Article Command
    Input    B

Input Inproceedings Command
    Input    C

Input Exit Command
    Input    2

Book Input Credentials
    [Arguments]
    ...    ${key}
    ...    ${title}
    ...    ${author}
    ...    ${publisher}
    ...    ${year}
    ...    ${volume}
    ...    ${number}
    ...    ${pages}
    ...    ${month}
    ...    ${note}
    Input    ${key}
    Input    ${title}
    Input    ${author}
    Input    ${EMPTY}
    Input    ${publisher}
    Input    ${year}
    Input    ${volume}
    Input    ${number}
    Input    ${pages}
    Input    ${month}
    Input    ${note}