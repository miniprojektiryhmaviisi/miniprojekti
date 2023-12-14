*** Settings ***
Resource      resource.robot
Test Setup    Prepare DB

*** Test Cases ***
Delete all references
    Input Delete Command
    Input Delete Confirmation
    Input View Command
    Input Exit Command
    Execute App
    Output Should Contain    No references
