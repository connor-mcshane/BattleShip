## Small Fixes

Reducing lines of code if possible.

## Design Fixes
1. Make the text parser more sophisticated. The Simulation class is a bit messy,
if should really just take the input file, read the commands and then write
the output.

2. Could consider using a Bitarray for each x line for the grid, this could 
save memory.

3. Also would revise the ship record system of having object references.
It would be better to have an interface and not use an object reference,
in case we wanted to use a *DataBase*. We could mock a database with a 
dictionary and then the interface would essentially be the same.

4. If the ship, did the path finding, then we could possibly have a multithreaded
implementation. But then the file reads are sequential so
probably not much to be gained.