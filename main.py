def tic_tac_toe():
    print("welcome to tic tac toe")
    user = input("type play to play or quit to quit")
    if user == "play":
        print("decide who's going first")
        game = ['-','-','-']['-','-','-']['-','-','-']
        print "here are the cordinates to enter for each position on ur game board for refrence: /n[.(1,1)   (1,2)   (1,3)] \n[(2,1)   (2,2)   (2,3)] \n [(3,1)   (3,2)   (3,3)]”*
        for row in game:
            print(row)
            guess = input("put in a coordinate with no spaces, parnethesis, or commas")
            for num in guess:
                num = num - 1
                if **gameboard[guess[0][guess[1]** = '-':
                    **gameboard[guess[0][guess[1]** = 'X"
                    player_2 = input("ok player 2 now yout turn")
                    if **gameboard[guess[0][guess[1]** = '-':
                    **gameboard[guess[0][guess[1]** = 'O'
                else:
                    print "this space is taken please try another space"
