# OHTU miniproject
[![Pipeline](https://github.com/miniprojektiryhmaviisi/miniprojekti/actions/workflows/pipeline.yml/badge.svg)](https://github.com/miniprojektiryhmaviisi/miniprojekti/actions/workflows/pipeline.yml)
[![codecov](https://codecov.io/gh/miniprojektiryhmaviisi/miniprojekti/graph/badge.svg?token=I1MPE3DZNF)](https://codecov.io/gh/miniprojektiryhmaviisi/miniprojekti)

## Product backlog
- [Product backlog](https://docs.google.com/spreadsheets/d/1JvMNbB3Pf6gLMOIwofjEcqaUdB0R7BNAem1QfK49YM4/edit#gid=0)

## Sprint backlogs
- [Sprints](https://docs.google.com/spreadsheets/d/1JvMNbB3Pf6gLMOIwofjEcqaUdB0R7BNAem1QfK49YM4/edit#gid=2050081642)

## Product's Definition of Done
*The requirement has been analyzed (acceptance criteria created), planned (divided into technical tasks), programmed, tested (with minimum coverage of 80%), testing automated (CI-pipeline), documented (with Readme file) and merged into main production branch.*

## Installation instructions & user manual

- Install dependencies in terminal:
  ```poetry install```
- Move into virtual environment:
   ```poetry shell```
- Start the application:
  ```python3 src/main.py```
  
- Select 0 to add a new reference, 1 to view your references.
- Select the format of the reference by entering A, B or C for book, article or inproceedings reference.
- Answer the asked fields. 
- Press 2 to close the application.

## Feature list
- *User can store book, article and inproceedings references*
- *Programs informs the user of invalid inputs*
- *User can view their saved references in a list*

