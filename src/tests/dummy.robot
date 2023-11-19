*** Settings **
Resource  resource.robot

*** Test Cases ***
Increase Counter Once
    Counter Value Should Be  0
    Add
    Counter Value Should Be  1
