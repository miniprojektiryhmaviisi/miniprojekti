*** Settings ***
Resource        resource.robot
Test Setup      Input Add Reference Command

*** Test Cases ***
Add Book Reference with valid input
    Input Book Command
    Book Input Credentials
    ...    somekeyy
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
    Ask Bookform
    Output Should Contain    New reference added!

# Add Book Reference with already used cite key
#     Input Book Command
#     Book Input Credentials
#     ...    somekeyy
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
#     Ask Bookform
#     Output Should Contain   Cite key must be unique!

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
