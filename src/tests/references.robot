*** Settings ***
Resource        resource.robot

Test Setup      Input Add Reference Command


*** Test Cases ***
Add Book Reference With Valid Input
    ${key}=    Get Time    epoch
    Log    Generated key: ${key}
    Input Book Command
    Book Input Credentials
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
    Input Exit Command
    Ask Form
    Output Should Contain    New reference added!

Add Article Reference With Valid Input
    ${key}=    Get Time    epoch
    Log    Generated key: ${key}
    Input Article Command
    Article Input Credentials
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
    Input Exit Command
    Ask Form
    Output Should Contain    New reference added!

# Add Inproceedings Reference With Valid Input
#     ${key}=    Get Time    epoch
#     Log    Generated key: ${key}
#     Input Inproceedings Command
#     Inproceedings Input Credentials
#     ...    ${key}
#     ...    Operating Systems
#     ...    Stallings
#     ...    MacMillan
#     ...    1991
#     ...    682
#     ...    1
#     ...    100-108
#     ...    123
#     ...    123
#     ...    123
#     ...    123
#     ...    123
#     ...    123
#     ...    123
#     Input Exit Command
#     Ask Form
#     Output Should Contain    New reference added!

# Add Empty Reference For Non-Optional Fields
#     ${key}=    Get Time    epoch
#     Log    Generated key: ${key}
#     Input Book Command
#     Book Input Credentials 
#     #...    ${EMPTY}
#     ...    key
#     ...    Operating Systems
#     ...    Stallings
#     ...    MacMillan
#     ...    1991
#     ...    682
#     ...    1
#     ...    100-108
#     ...    12
#     ...    ${EMPTY}
#     Input Exit Command
#     #tähän asti output on []
#     Ask Form
#     #jos pakollinen kenttä esim key kuten yllä, on tyhjä, tulee vaan "IndexError: pop from empty list" eikä se jatka siitä
#     #eteenpäin, siihen kohtaan jossa kerrotaan että field empty jne.
#     Output Should Contain    Field cannot be empty. Please provide a valid input.

# Add Book Reference with already used cite key
#    Input Book Command
#    Book Input Credentials
#    ...    somekeyy
#    ...    Operating Systems
#    ...    Stallings
#    ...    MacMillan
#    ...    1991
#    ...    682
#    ...    1
#    ...    100-108
#    ...    12
#    ...    ${EMPTY}
#    Input Exit Command
#    Ask Form
#    Output Should Contain    Cite key must be unique!

# Login With Incorrect Password
#    Input Credentials    kalle    kalle12369
#    Output Should Contain    Invalid username or password

# Login With Nonexistent Username
#    Input Credentials    Nonexistent    kalle123
#    Output Should Contain    Invalid username or password

# *** Keywords ***
# Create User And Input Login Command
#    Create User    kalle    kalle123
#    Input Login Command

# *** Keywords ***
# Create User And Input New Command
#    Create User    kalle    kalle123
#    Input Login Command
