*** Settings ***
Resource  resource.robot
Test Setup  Input 0 Command

*** Test Cases ***
Saved 
    Input Credentials  kalle  kalle123
    Output Should Contain  Logged in


Login With Incorrect Password
    Input Credentials  kalle  kalle12369
    Output Should Contain  Invalid username or password

Login With Nonexistent Username
    Input Credentials  Nonexistent  kalle123
    Output Should Contain  Invalid username or password


*** Keywords ***
Create User And Input Login Command
    Create User  kalle  kalle123
    Input Login Command

*** Keywords ***
Create User And Input New Command
    Create User  kalle  kalle123
    Input Login Command
