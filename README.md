# Chess_AI
A python based AI programme that decides the next move when a chess board and the side to move is given.

DISCLAIMER: This is by no means the most efficient way to design chess AI, neither is it very intelligent.
This was made as a proof of concept of minimax theory and how it can be applied to a chess game.

GENERAL RUNNING:
The idea is to use the concept of class, to make an instance of a board.
Use helper functions, to manipulate the board to produce other possible states from the board instance.
Score it using a heuristic(defined by myself)
Use minimax method of graph search to decide on the best move.
