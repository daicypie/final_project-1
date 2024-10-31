from random import randrange

def display_board(board):
    for row in board:
        print("+-------" * 3 + "+")
        print("|       " * 3 + "|")
        print("|   " + "   |   ".join(map(str, row)) + "   |")
        print("|       " * 3 + "|")
    print("+-------" * 3 + "+")

def enter_move(board):
    valid = False
    while not valid:
        move = input("Введіть число (1-9): ")
        if len(move) == 1 and move in '123456789':
            move = int(move) - 1
            row, col = divmod(move, 3)
            if board[row][col] not in ["O", "X"]:
                board[row][col] = "O"
                valid = True
            else:
                print("Поле зайнято, спробуйте ще раз.")
        else:
            print("Неправильний хід, спробуйте ще раз.")

def make_list_of_free_fields(board):
    free_fields = [(r, c) for r in range(3) for c in range(3) if board[r][c] not in ["O", "X"]]
    return free_fields

def victory_for(board, sign):
    win_conditions = [
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)],
    ]
    for condition in win_conditions:
        if all(board[r][c] == sign for r, c in condition):
            return True
    return False

def draw_move(board):
    free_fields = make_list_of_free_fields(board)
    move = free_fields[randrange(len(free_fields))]
    board[move[0]][move[1]] = "X"

board = [[1, 2, 3], [4, "X", 6], [7, 8, 9]]

while True:
    display_board(board)
    if victory_for(board, "X"):
        print("Комп'ютер вийграв! (┬┬﹏┬┬))")
        break
    if not make_list_of_free_fields(board):
        print("Нічия!")
        break
    enter_move(board)
    if victory_for(board, "O"):
        display_board(board)
        print("Ти вийграв! (～￣▽￣)～")
        break
    if not make_list_of_free_fields(board):
        print("Нічия!")
        break
    draw_move(board)