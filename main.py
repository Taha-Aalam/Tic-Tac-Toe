# tic-tac-toe game by Taha Aalam
# using loops functions and lists
# importing required modules
import os
import time
import random

# define board
board = [" ", " ", " ", " ", "O", " ", " ", " ", " "]


# printing the header
def print_header():
    print("""Tic - Tac - Toe                                                                         1 | 2 | 3
Welcome Player, to win a game of Tic-Tac-Toe you need to get three in a row             ---------
your choices are defined, They must be from 1 to 9                                      4 | 5 | 6
                                                                                        ---------
                                                                                        7 | 8 | 9
            """)


# printing the board board
def print_board():
    print("    |    |    ")
    print(" " + board[0] + "  |  " + board[1] + " |  " + board[2])
    print("    |    |    ")
    print("----|----|----")
    print("    |    |    ")
    print(" " + board[3] + "  |  " + board[4] + " |  " + board[5])
    print("    |    |    ")
    print("----|----|----")
    print("    |    |    ")
    print(" " + board[6] + "  |  " + board[7] + " |  " + board[8])
    print("    |    |    ")


# function to check if the player or Ai finished the game
def is_winner(board, player):
    if (board[0] == player and board[1] == player and board[2] == player) or \
            (board[3] == player and board[4] == player and board[5] == player) or \
            (board[6] == player and board[7] == player and board[8] == player) or \
            (board[0] == player and board[3] == player and board[6] == player) or \
            (board[1] == player and board[4] == player and board[7] == player) or \
            (board[2] == player and board[5] == player and board[8] == player) or \
            (board[0] == player and board[4] == player and board[8] == player) or \
            (board[2] == player and board[4] == player and board[6] == player):
        return True
    else:
        return False


# function to check for tie
def is_board_full(board):
    if " " in board:
        return False
    else:
        return True


# function to get input from the user
def get_players_input(board, player):
    while True:
        os.system("cls")
        print_header()
        print_board()
        choice = input("Enter please chose an empty space for {0}: ".format(player))
        choice = int(choice)
        if (1 <= choice <= 9):
            choice -= 1
            if board[choice] == " ":
                board[choice] = player
                break
            else:
                print("Please choose a empty space.")
                time.sleep(2)
        else:
            print("Worng input, please enter a number from 1 to 9")
            time.sleep(2)


# functoion to get Ai move
def get_computer_move(board, player):
    # check if Ai can win
    player = "O"
    if board[0] == " " and board[1] == player and board[2] == player:
        return 0
    elif board[3] == " " and board[4] == player and board[5] == player:
        return 3
    elif board[6] == " " and board[7] == player and board[8] == player:
        return 6
    elif board[0] == " " and board[3] == player and board[6] == player:
        return 0
    elif board[1] == " " and board[4] == player and board[7] == player:
        return 1
    elif board[2] == " " and board[5] == player and board[8] == player:
        return 2
    elif board[0] == " " and board[4] == player and board[8] == player:
        return 0
    elif board[2] == " " and board[4] == player and board[6] == player:
        return 2
    elif board[0] == player and board[1] == " " and board[2] == player:
        return 1
    elif board[3] == player and board[4] == " " and board[5] == player:
        return 4
    elif board[6] == player and board[7] == " " and board[8] == player:
        return 7
    elif board[0] == player and board[3] == " " and board[6] == player:
        return 3
    elif board[1] == player and board[4] == " " and board[7] == player:
        return 4
    elif board[2] == player and board[5] == " " and board[8] == player:
        return 5
    elif board[0] == player and board[4] == " " and board[8] == player:
        return 4
    elif board[2] == player and board[4] == " " and board[6] == player:
        return 4
    elif board[0] == player and board[1] == player and board[2] == " ":
        return 2
    elif board[3] == player and board[4] == player and board[5] == " ":
        return 5
    elif board[6] == player and board[7] == player and board[8] == " ":
        return 8
    elif board[0] == player and board[3] == player and board[6] == " ":
        return 6
    elif board[1] == player and board[4] == player and board[7] == " ":
        return 7
    elif board[2] == player and board[5] == player and board[8] == " ":
        return 8
    elif board[0] == player and board[4] == player and board[8] == " ":
        return 8
    elif board[2] == player and board[4] == player and board[6] == " ":
        return 6

    player = "X"
    # check if player can win
    if board[0] == " " and board[1] == player and board[2] == player:
        return 0
    elif board[3] == " " and board[4] == player and board[5] == player:
        return 3
    elif board[6] == " " and board[7] == player and board[8] == player:
        return 6
    elif board[0] == " " and board[3] == player and board[6] == player:
        return 0
    elif board[1] == " " and board[4] == player and board[7] == player:
        return 1
    elif board[2] == " " and board[5] == player and board[8] == player:
        return 2
    elif board[0] == " " and board[4] == player and board[8] == player:
        return 0
    elif board[2] == " " and board[4] == player and board[6] == player:
        return 2
    elif board[0] == player and board[1] == " " and board[2] == player:
        return 1
    elif board[3] == player and board[4] == " " and board[5] == player:
        return 4
    elif board[6] == player and board[7] == " " and board[8] == player:
        return 7
    elif board[0] == player and board[3] == " " and board[6] == player:
        return 3
    elif board[1] == player and board[4] == " " and board[7] == player:
        return 4
    elif board[2] == player and board[5] == " " and board[8] == player:
        return 5
    elif board[0] == player and board[4] == " " and board[8] == player:
        return 4
    elif board[2] == player and board[4] == " " and board[6] == player:
        return 4
    elif board[0] == player and board[1] == player and board[2] == " ":
        return 2
    elif board[3] == player and board[4] == player and board[5] == " ":
        return 5
    elif board[6] == player and board[7] == player and board[8] == " ":
        return 8
    elif board[0] == player and board[3] == player and board[6] == " ":
        return 6
    elif board[1] == player and board[4] == player and board[7] == " ":
        return 7
    elif board[2] == player and board[5] == player and board[8] == " ":
        return 8
    elif board[0] == player and board[4] == player and board[8] == " ":
        return 8
    elif board[2] == player and board[4] == player and board[6] == " ":
        return 6

    # if player choose 7
    if board[6] == "X":
        if board[2] == " ":
            return 2
        if board[5] == "X":
            if board[0] == " ":
                return 0
        if board[1] == "X":
            if board[8] == " ":
                return 8

    # if player choose 1
    if board[0] == "X":
        if board[8] == " ":
            return 8
        if board[5] == "X":
            if board[6] == " ":
                return 6
        if board[7] == "X":
            if board[2] == " ":
                return 2

    #  if player choose 3
    if board[2] == "X":
        if board[6] == " ":
            return 6
        if board[3] == "X":
            if board[8] == " ":
                return 8
        if board[7] == "X":
            if board[0] == " ":
                return 0

    # if player choose 9
    if board[8] == "X":
        if board[0] == " ":
            return 0
        if board[1] == "X":
            if board[6] == " ":
                return 6
        if board[3] == "X":
            if board[2] == " ":
                return 2

    # if player choose 2
    if board[1] == "X":
        if board[6] == " ":
            return 6

    # if player choose 4
    if board[3] == "X":
        if board[8] == " ":
            return 8

    # if player choose 6
    if board[5] == "X":
        if board[0] == " ":
            return 0

    # if player chosse 8
    if board[7] == "X":
        if board[2] == " ":
            return 2

    # if the above code fails send random value
    # Sending random empty value
    while True:
        move = random.randint(0, 8)
        if board[move] == " ":
            return move
            break


while True:
    # getting the input from the player 1
    os.system("cls")
    print_header()
    print_board()
    get_players_input(board, "X")

    # check if the player 1 has won the game
    if is_winner(board, "X"):
        os.system("cls")
        print_header()
        print_board()
        print("Congratulations, Player wins.")
        break

    # check for tie
    if is_board_full(board):
        os.system("cls")
        print_header()
        print_board()
        print("Tie!!!")
        break

    # Ai's move
    os.system("cls")
    print_header()
    print_board()
    move = get_computer_move(board, "X")
    board[move] = "O"

    # check if Ai has won the game
    if is_winner(board, "O"):
        os.system("cls")
        print_header()
        print_board()
        print("Computer wins, Better luck next time.")
        break

    #check for tie
    if is_board_full(board):
        os.system("cls")
        print_header()
        print_board()
        print("Tie!!!")
        break
