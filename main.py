def tic_tac_toe():
    print("welcome to tic tac toe")
    user = input("type 'play' to play or 'quit' to quit ")
    if user == "play":
        print("decide who's going first")
        print("here are the cordinates to enter for each position on ur game board for reference:")
        print("[(1,1)   (1,2)   (1,3)] \n")
        print("[(2,1)   (2,2)   (2,3)] \n")
        print("[(3,1)   (3,2)   (3,3)] \n")
        print(" ~~~~~~~~~~STARTING GAME~~~~~~~~~~")
        gameboard = [['-','-','-'],['-','-','-'],['-','-','-']]
        gameover = False
        while gameover == False:
            move_player('X', gameboard)
            gameover = three_in_a_row('X', gameboard, gameover)
            if gameover:
                for row in gameboard:
                    print(row)
                break
            move_player('O', gameboard)
            gameover = three_in_a_row('O', gameboard, gameover)
            if gameover:
                for row in gameboard:
                    print(row)
                break
            gameover = tie_game(gameboard, gameover)
            if gameover:
                for row in gameboard:
                    print(row)
                break
        tic_tac_toe()

def move_player(player, gameboard):
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
        
def three_in_a_row (player, gameboard, gameover):
    for row in gameboard:
        if all([spot == player for spot in row]):
            gameover = True
            print("%s wins!!!" %player)
            return(gameover)
    for column in range(len(gameboard)):
        won = True
        for row in range(len(gameboard)):
            if gameboard[row][column] != player:
                won = False
                break
        if won is True:
            gameover = True
            print("%s wins!!!" %player)
            return(gameover)
    if gameboard[0][0] == player and gameboard[1][1] == player and gameboard[2][2] == player:
            gameover = True
            print("%s wins!!!" %player)
            return(gameover)
    if gameboard[0][2] == player and gameboard[1][1] == player and gameboard[2][0] == player:
            gameover = True
            print("%s wins!!!" %player)
            return(gameover)

def tie_game(gameboard, gameover):
    for row in gameboard:
        if "-" in row:
            gameover = False
            return(gameover)
    gameover = True
    return(gameover)

    
     
if __name__ == '__main__':
    tic_tac_toe()
