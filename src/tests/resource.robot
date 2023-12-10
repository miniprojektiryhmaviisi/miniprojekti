*** Settings ***
Library    ../ReferencesLibrary.py
Library    ../BibLibrary.py


*** Keywords ***
Input Add Reference Command
    Input    0

Input View Command
    Input    1

Input Search Command
    Input    2

Input Bibtex Command
    Input    3

Input Delete Command
    Input    4

Input Exit Command
    Input    5

Input Book Command
    Input    A

Input Article Command
    Input    B

Input Inproceedings Command
    Input    C

Input Delete Confirmation
    Input    delete

Input Single Reference Deletion Command
    Input    d

Book Input Details
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

Book Input Details Two Keys
    [Arguments]
    ...    ${key}
    ...    ${key2}
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
    Input    ${key2}
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

Book Input Details Mandatory Empty
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
    Input    ${EMPTY}
    Input    ${year}
    Input    ${volume}
    Input    ${number}
    Input    ${pages}
    Input    ${month}
    Input    ${note}

Article Input Details
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

Inproceedings Input Details
    [Arguments]
    ...    ${key}
    ...    ${title}
    ...    ${author}
    ...    ${publisher}
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
    ...    ${note}

    Input  ${key}
    Input  ${title}
    Input  ${booktitle}
    Input  ${author}
    Input  ${EMPTY}
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
    
Input Both Search Details
    [Arguments]
    ...    ${author}
    ...    ${title}
    Input    ${author}
    Input    ${title}

Input Book Key
    [Arguments]
    ...    ${book_key}
    Input    ${book_key}
    Input    ${EMPTY}

Input All Keys
    [Arguments]
    ...    ${book_key}
    ...    ${article_key}
    ...    ${inproceedings_key}
    Input    ${book_key}
    Input    ${article_key}
    Input    ${inproceedings_key}
    Input    ${EMPTY}

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