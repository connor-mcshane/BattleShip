# BattleShip
Battleship simulation. An input text file is passed in and then an output file is written with the final state of the simulation

### Version
This program was developed with Python 3 and should not require any additional python packages to be installed

### Usage
To use the program as a command lind utility simply enter in a command prompt 

``` >>> python  command_line_sim.py  input_file_path output_file_path ```

There are some demo files which can be found in test_files e.g

``` python  command_line_sim.py  tests/test_files/input_1.txt tests/test_files/output_1.txt ```

Also there is a suite of unit tests that can be run from the base directory of the project.
``` python -m unittest discover tests ```

### Notes on the code logic
The Simulation instance is used to parse in the input text and create and interace with a Gameboard instance. The gameboard instance will then create a gameboard, and manage the addition, movement and sinking of Ship instances.

### Notes on coding style
The author attempted to use PEP 8 coding style where possible. Also the author tried to ensure that the code is readable as much as possible.



