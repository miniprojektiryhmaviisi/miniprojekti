*** Settings ***
Resource      resource.robot
Test Setup    Prepare DB

*** Test Cases ***
Test Listing Order
    Input View Command
    Input Exit Command
    Execute App
    Order Should Be    Author${SPACE*7}: AStallings    Author${SPACE*7}: KStallings
    Order Should Be    Author${SPACE*7}: KStallings    Author${SPACE*7}: ZStallings

Test Bibtex Order
    Input Bibtex Command
    Input Exit Command
    Execute App
    Order In File Should Be    file.bib    author = \{AStallings\},    author = \{KStallings\},
    Order In File Should Be    file.bib    author = \{KStallings\},    author = \{ZStallings\},

*** Keywords ***
Prepare DB
    Input Delete Command
    Input Delete Confirmation
    Input Add Reference Command
    Input Book Command
    Book Input Details
    ...    TestKeyZ
    ...    Operating Systems
    ...    ZStallings
    ...    MacMillan
    ...    1991
    ...    682
    ...    1
    ...    100-108
    ...    12
    ...    ${EMPTY}
    Input Add Reference Command
    Input Book Command
    Book Input Details
    ...    TestKeyA
    ...    Operating Systems
    ...    AStallings
    ...    MacMillan
    ...    1991
    ...    682
    ...    1
    ...    100-108
    ...    12
    ...    ${EMPTY}
    Input Add Reference Command
    Input Book Command
    Book Input Details
    ...    TestKeyK
    ...    Operating Systems
    ...    KStallings
    ...    MacMillan
    ...    1991
    ...    682
    ...    1
    ...    100-108
    ...    12
    ...    ${EMPTY}