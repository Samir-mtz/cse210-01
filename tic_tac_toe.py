board = [[1,2,3],[4,5,6],[7,8,9]]
position = {1:[0,0], 2:[0,1], 3:[0,2], 4:[1,0], 5:[1,1], 6:[1,2], 7:[2,0], 8:[2,1], 9:[2,2]}

def main():
    start()
    play()

def start():
    print("Welcome to the tic tac toe game!")
    show_board()

def show_board():
    for i in board:
        print("\t|", end='')
        for j in i:
            print(f"{j}|", end="")
        print("\n\t-------")

def play():
    i = 1
    while(i <= 9):
        if(i % 2 != 0):
            square = int(input("x's turn to choose a square (1-9): "))
            element = "x"
            if(can_choose_square(square)):
                mark(square, element)
                if(i>2):
                    if(check_board()):
                        show_board()
                        print("Player 1 wins")
                        exit()
                i += 1
            else:
                print("Place already taken, choose another square")
        else:
            square = int(input("o's turn to choose a square (1-9): "))
            element = "o"
            if(can_choose_square(square)):
                mark(square, element)
                if(i>2):
                    if(check_board()):
                        show_board()
                        print("Player 2 wins")
                        exit()
                i += 1
            else:
                print("Place already taken, choose another square")
        show_board()
    print("It's a tie")

def mark(square, element):
    x = position[square][0]
    y = position[square][1]
    board[x][y] = element

def can_choose_square(square):
    x = position[square][0]
    y = position[square][1]
    if(type(board[x][y]) == int):
        return True
    else:
        return False

def check_board():
    first = board[0][0]
    if(type(first) != int):
        if(board[0][1] == first and board[0][2] == first):
            return True
            
        if(board[1][0] == first and board[2][0] == first):
            return True
        if(board[1][1] == first and board[2][2] == first):
            return True

    first = board[0][1]
    if(type(first) != int):
        if(board[1][1] == first and board[2][1] == first):
            return True
            

    first = board[0][2]
    if(type(first) != int):
        if(board[1][2] == first and board[2][2] == first):
            return True
            
        if(board[1][1] == first and board[2][0] == first):
            return True

    first = board[1][0]
    if(type(first) != int):
        if(board[1][1] == first and board[1][2] == first):
            return True
            
    first = board[2][0]
    if(type(first) != int):
        if(board[2][1] == first and board[2][2] == first):
            return True
            
    return False

main()