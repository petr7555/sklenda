# Sklenda
A fun game developed in Python using Pygame.

# How to run
- `poetry install`
- `poetry run python Sklenda.py`

# Rules
This game has a similar principle to tic-tac-toe.  
You are provided with a board 4x4 and 16 "rocks". Your objective is to match a group of 4 same rocks, either horizontally in line or vertically in line. Square 2x2 also counts. Each rock is somehow different.  
They have 4 parameters:
1. shape: rounded / square
2. color: yellow / brown
3. dot: with / without
4. size: small / large

If the rocks in the group of 4 have all at least one same parameter, the person who created this group of 4 wins.

The game is for 2 players. The first player chooses a rock. Then is player 2's turn. They place the rock and choose a rock for player 1. Player 1 places a rock and chooses a rock for player 2 to be placed – and so on until the game ends.

The rocks do not have any owner. You can place the rock anywhere on the board. If – after you placed the rock – there is a valid group on the board, you are the winner. If the group is created during your opponent's turn, they are the winner.

Simple advice: follow the instructions on the screen.

Have fun!!!
