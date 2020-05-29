gameboard = [['-','-','-'],['-','-','-'],['-','-','-']]

def tic_tac_toe():
    print("welcome to tic tac toe")
    user = input("type 'play' to play or 'quit' to quit")
    if user == "play":
        print("decide who's going first")
        print("here are the cordinates to enter for each position on ur game board for reference:")
        print("[(1,1)   (1,2)   (1,3)] \n")
        print("[(2,1)   (2,2)   (2,3)] \n")
        print("[(3,1)   (3,2)   (3,3)] \n")
        print(" ~~~~~~~~~~STARTING GAME~~~~~~~~~~")
        move_player('X')
        move_player('O')

def move_player(player):
    print("this is the current gameboard")
    for row in gameboard:
        print(row)
    guess = list(input("Player %s put in the coordinates of your move. Please don’t use parenthesis, commas or spaces though. For example, if you want to take (1,2) just enter 12" %player))
    for index, num in enumerate(guess):
        guess[index] = int(num) - 1
    if gameboard[guess[0]][guess[1]] == '-':
        gameboard[guess[0]][guess[1]] = player
    else:
        print("this space is taken please try another space")
        move_player(player)
