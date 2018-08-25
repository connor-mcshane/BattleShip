## Bugs Fixes
- Need to fix path finding. (i.e movement sequence can be off the board and then back on the board)
fix just involves checking each movement to validate if its on the board.
- Need to "empty" the cell, once the ship has begun moving on a sequence (in case the ships moves back to the 
original spot).

## Design Fixes
1. Make the text parser more sophisticated. The Simulation class is a bit messy,
if should really just take the input file, read the commands and then write
the output.

2. Use a hashmap, to keep track of the ships and their positions.
