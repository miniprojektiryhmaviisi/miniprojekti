*** Settings ***
Resource      resource.robot
Test Setup    Prepare DB   

*** Test Cases ***
List all references
    Input View Command
    Input Exit Command
    Execute App
    Output Should Contain    \x1b[0m*・゜゜・*:.。..。.:*・゜・*:.。. .。.:*・゜゜・*\x1b[38;5;18;2m
    Output Should Contain    Book references
    Output Should Contain    \x1b[0m*・゜゜・*:.。..。.:*・゜・*:.。. .。.:*・゜゜・*\x1b[38;5;18;2m
    Output Should Contain    Cite Key\ \ \ \ \ : TestKey
    Output Should Contain    Author\ \ \ \ \ \ \ : Stallings
    Output Should Contain    Title\ \ \ \ \ \ \ \ : Operating Systems
    Output Should Contain    Publisher\ \ \ \ : MacMillan
    Output Should Contain    Year\ \ \ \ \ \ \ \ \ : 1991
    Output Should Contain    Volume\ \ \ \ \ \ \ : 682
    Output Should Contain    Number\ \ \ \ \ \ \ : 1
    Output Should Contain    Pages\ \ \ \ \ \ \ \ : 100-108
    Output Should Contain    Month\ \ \ \ \ \ \ \ : 12
    Output Should Contain    \x1b[0m*・゜゜・*:.。..。.:*・゜・*:.。. .。.:*・゜゜・*\x1b[38;5;18;2m


*** Keywords ***
Prepare DB
    Input Delete Command
    Input Delete Confirmation
    Input Add Reference Command
    Input Book Command
    Book Input Details
    ...    TestKey
    ...    Operating Systems
    ...    Stallings
    ...    MacMillan
    ...    1991
    ...    682
    ...    1
    ...    100-108
    ...    12
    ...    ${EMPTY}