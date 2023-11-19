*** Settings **
Resource  resource.robot

*** Test Cases ***
Increase Counter Once
    Value Should Be  0
    Add  1
    Value Should Be  1

Increase Counter Once By Two And Multiply By Four
    Value Should Be  0
    Add  2
    Multiply  4
    Value Should Be  8
