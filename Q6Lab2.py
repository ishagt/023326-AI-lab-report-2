#6.	WAP in Python to calculate the heuristic value of the states for Tic-Tac-Toe as follows
#Heuristic function:
#e(p)= No. of complete rows, columns or diagonals are still open for player p – (No. of complete rows, columns or diagonals are still open for opponent)
def heuristic(board, player):
    opponent = 'O' if player == 'X' else 'X'
    def is_open(line):
        return all(cell != opponent for cell in line)
    open_lines_player = 0
    open_lines_opponent = 0
    # Check rows and columns
    for i in range(3):
        if is_open(board[i]):
            open_lines_player += 1
        if is_open([board[j][i] for j in range(3)]):
            open_lines_player += 1
    # Check diagonals
    if is_open([board[i][i] for i in range(3)]):
        open_lines_player += 1
    if is_open([board[i][2 - i] for i in range(3)]):
        open_lines_player += 1
    # Repeat for opponent
    for i in range(3):
        if is_open(board[i]):
            open_lines_opponent += 1
        if is_open([board[j][i] for j in range(3)]):
            open_lines_opponent += 1
    if is_open([board[i][i] for i in range(3)]):
        open_lines_opponent += 1
    if is_open([board[i][2 - i] for i in range(3)]):
        open_lines_opponent += 1
    return open_lines_player - open_lines_opponent
# Example usage
board = [
    ['X', 'O', 'X'],        
    [' ', 'X', ' '],
    ['O', ' ', ' ']
]
player = 'X'
h_value = heuristic(board, player)
print("Heuristic value for player", player, "is:", h_value)
#output:
#Heuristic value for player X is: 2
