*** Settings ***
Library     ../ReferencesLibrary.py


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

Article Input Credentials
    [Arguments]
    ...    ${key}
    ...    ${title}
    ...    ${author}
    ...    ${journal}
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
    Input    ${journal}
    Input    ${year}
    Input    ${volume}
    Input    ${number}
    Input    ${pages}
    Input    ${month}
    Input    ${note}

Inproceedings Input Credentials
    [Arguments]
    ...    ${key}
    ...    ${author}
    ...    ${title}
    ...    ${booktitle}
    ...    ${year}
    ...    ${editor}
    ...    ${volume}
    ...    ${number}
    ...    ${series}
    ...    ${pages}
    ...    ${address}
    ...    ${month}
    ...    ${organization}
    ...    ${publisher}
    ...    ${note}

    Input  ${key}
    Input  ${author}
    Input  ${EMPTY}
    Input  ${title}
    Input  ${booktitle}
    Input  ${year}
    Input  ${editor}
    Input  ${volume}
    Input  ${number}
    Input  ${series}
    Input  ${pages}
    Input  ${address}
    Input  ${month}
    Input  ${organization}
    Input  ${publisher}
    Input  ${note}
    

