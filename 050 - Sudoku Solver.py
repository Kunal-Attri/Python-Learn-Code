# Sudoku Solver

# let's first get an example sudoku

# make an array to denote it, mark empty spaces as 0
    # cols1  2  3  4  5  6  7  8  9         
# board = [[6, 0, 0, 0, 0, 0, 0, 4, 0],       # rows 1
#          [1, 8, 0, 0, 0, 3, 5, 0, 0],       # 2
#          [3, 0, 7, 0, 0, 0, 6, 8, 0],       # 3
#          [7, 0, 8, 0, 0, 0, 0, 6, 0],       # 4
#          [0, 0, 3, 4, 0, 0, 0, 0, 0],       # 5
#          [0, 0, 0, 0, 5, 2, 0, 3, 0],       # 6
#          [0, 0, 0, 0, 4, 1, 0, 7, 9],       # 7
#          [0, 0, 0, 3, 2, 0, 0, 0, 0],       # 8
#          [0, 0, 0, 0, 0, 0, 2, 0, 0]]       # 9

# lets take board input from user
print("Enter board rows one by one, empty spaces as 0. eg. Row 1: 6 0 0 0 0 0 0 4 0")
board = []
print()
for i in range(9):
    row = input(f"Row {i + 1}: ").split()
    l = [int(x) for x in row]
    board.append(l)


# function to print board on terminal
def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:       # for separation box rows
            print("- - - - - - - - - - -")
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:       # for separation box cols
                print("| ", end = "")
            if j == 8:      # last column
                print(board[i][j] if board[i][j] != 0 else " ")
                # printing last colm no if not 0, else empty space
            else:
                print(str(board[i][j]) if board[i][j] != 0 else " ", end = "")
                # printing other col no.s if not 0, else empty space
                print(" ", end = "")

# lets test this print function
print("\nQuestion:")
print_board(board)
# looks perfect

# Function to find empty spaces
def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return i, j     # row, col
    return False        # if no empty spaces

# Function to check if a no input is valid or not
def valid(board, num, position):
    # checking Row wise
    for i in range(len(board[0])):
        if board[position[0]][i] == num and position[1] != i:
            return False

    # checking Column wise
    for i in range(len(board[0])):
        if board[i][position[1]] == num and position[0] != i:
            return False

    # checking Block wise
    box_x = position[1] // 3        # position of box
    box_y = position[0] // 3        # eg, position of middle box is 1,1
    for i in range(box_y * 3, box_y * 3 + 3):       # from 3, 4, 5, center box eg
        for j in range(box_x * 3, box_x * 3 + 3):       # from 3, 4, 5
            if board[i][j] == num and (i, j) != position:
                return False
    return True     # if valid


# Function to solve the board
# using recursive approach
def solve(board):
    find = find_empty(board)
    if not find:        # if the board has been solved, and there are no empty spaces
        return True
    else:
        row, col = find
    for i in range(1, 10):
        if valid(board, i, (row, col)):     # checking which no fits in that empty cell
            board[row][col] = i
            if solve(board):        # if the board is solved now, i.e. recursively solving it
                return True
            board[row][col] = 0
    return False        # if the entered value(in for loop) is wrong

# lets test it
print("\nSolution:")
solve(board)
print_board(board)


# Thank You !!!
