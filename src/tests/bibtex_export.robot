*** Settings ***
Resource        resource.robot

*** Test Cases ***
Export all references
    Input Bibtex Command
    Input Exit Command
    Ask Form
    Parse And Check Bibfile