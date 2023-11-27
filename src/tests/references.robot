*** Settings ***
Resource        resource.robot

Test Setup      Input Add Reference Command


*** Test Cases ***
Add Book Reference with valid input
    Book Input Credentials
    ...    somekey
    ...    Stallings
    ...    Nonexistent
    ...    Operating Systems
    ...    1991
    ...    MacMillan
    ...    682
    ...    1
    ...    100-108
    ...    October Nonexistent
    Output Should Contain    Your entry has been saved

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
