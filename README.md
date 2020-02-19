# 8_Puzzle_-Problem
 
The puzzle consists of an area divided into a grid, 3 by 3 for the 8-puzzle. On each grid square is a tile, expect for one square which remains empty. Thus, there are eight tiles in the 8-puzzle.

This problem is solved by searching for solution, that leads from the initial state to the goal state that involves a sequence of actions (tile moves).

8 puzzle can be solved by using A* search algorithm in 2 different heuristic methods.

        1. Manhattan Distance
        2. Misplaced Tiles
Manhattan Distance:

1.Initially the Manhattan distance from initial state to goal state is calculated using the function calculateManhattanDistance() 2.CalculateManhattanDistance() function accepts generated nodes and Goal State as for the generated nodes. 3.After the manhattan distance is calculated the node is stored in a heap data structure. 4. Nodes in the heap are checked if they are the goal else the next set of possible child states are generated using the function Nextnodes(). 5. If any of the existing states match with the goal state then the best path to that state is found using the function findpath().

Miplaced Tiles:

The Hamming distance is the total number of misplaced tiles.
This heuristic is admissible since the total number of moves to order the tiles correctly is at least the number of misplaced tiles 3. Each tile not in place must be moved at least once
