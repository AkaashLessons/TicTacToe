# Tic-Tac-Toe
Beginner Command-Line Tic-Tac-Toe
These are the instructions to follow:
For this assignment, we’re going to be building out a game of tic-tac-toe. It will be a two-player game (so person vs person instead of person vs computer)!

*One important thing to note is how we’ll be representing the tic-tac-toe board. When we play on paper, it’s 3 rows of 3
In code we’ll represent that as a list of 3 lists. For example, it could look something like this:*

[

    ['x', 'o', 'x'],
    
    ['o', '-', '-'],
    
    ['x', 'o', '-']
    
]

## STEP 1: Setting up our game
* First thing’s first. Let’s **print out a welcome message** for our users. Something like *“Welcome to tic-tac-toe!”*
* Use the menu we created in the last steps of hangman to create something similar here *(“Type ‘play’ to play and ‘quit’ to quit”)*. You can decide to put it in a function off the bat or do it later.
* Tell the users *“Decide who is going first and second”*
* Start by **creating a variable** that represents our game board. As discussed above, it’ll be a list of 3 lists that hold 3 elements (3 rows of 3 X’s or O’s)
* **Hint:** We start with every spot on the board being open. Let’s represent these as *‘-’* so start by **making one list of 3 hyphens: [‘-’,’-’,’-’] and then making a list comprised of 3 of those**

## STEP 2: Let X choose a spot
* The users probably won’t know how we index starting at 0 in python so let them put in coordinates from 1-3 instead of 0-2 (**This just means that when we go to store their move in our nested list, we’ll subtract one from each coordinate**)
* Let’s go back and right after they choose to play and show them what each coordinate corresponds to. Basically just print the following: *“Here are the coordinates to enter for each position on our game board as a reference: \n
            [(1,1)   (1,2)   (1,3)] \n
	[(2,1)   (2,2)   (2,3)] \n
	[(3,1)   (3,2)   (3,3)]”*
* First, we will **print out our game board** so the user knows what positions are taken. ***We need to loop through the outer list printing each each row in the board***
* Now, **prompt the user to put in the coordinates of where they want to move**
* We have to instruct the user to just write the two numbers with no parenthesis, commas or spaces ***so if they want to move to (1,2) they should enter 12.*** I.e use this line *coords = list(input(“Player X put in the coordinates of your move. Please don’t use parenthesis, commas or spaces though. For example, if you want to take (1,2) just enter 12”))*
* Now, ***the user’s coordinates are stored in a list.*** We need to check in our game-board list if that spot is open. 
* We access the spot they typed using **gameboard[coords[0]-1][coords[1]-1]** *(-1 comes from the fact that they use 1-3 not 0-2 for indexing)*
* We need to check if the value at this spot == ‘-’ *(it’s empty)*. If it is empty, put an ‘X’ in that spot. ***gameboard[coords[0]-1][coords[1]-1]  = ‘X’***
* If the spot isn’t empty, tell the user *“That spot is taken. Please input coordinates of an empty spot”*
* We should also utilize **try-except** here because if the user puts in invalid coordinates, we'll get an error and we need to tell them *“please put in coordinates from 1-3, using no spaces, commas, or parentheses”*


## STEP 3: Now O has to choose a spot
* This will basically look identical to 2-3 in step 2 except we replace ‘X’ with ‘O’
* If you want to be really ~ efficient ~ **create a helper function called move that takes in the game board and the player letter and executes step 2-3, putting the player letter where necessary**

## STEP 4: What is our “while” condition?
* Just like with hangman we’ll run a core loop while the game hasn’t ended yet
* The difference here is that there are multiple cases in which the game has ended that we have to check for
  * X won (3 X’s in a row horizontally, vertically, or diagonally)
  * O won (3 O’s in a row horizontally, vertically, or diagonally)
  * Tie (no one won but there are no empty spots)
* We’ll need to come up with a way to check for each of these, but first let’s **create a boolean called gameover and initialize it as False.** We’ll keep asking the user to input coordinates ***while the game isnt over so while gameover is False***
* **Add this while clause to the code you’ve already written**
* Inside the while clause we have X take a turn and then we have O take a turn
*(included in this turn-taking is printing out the gameboard). If you created a move function like recommended this will just look like move(gameboard,’X’) then move(gameboard, ‘O’)*

## STEP 5: Check if there are 3 in a row
* **Create a function called three_in_a_row that takes in the player letter, the game board, and gameover**
* Think of all the cases of 3 in a row:

Horizontally: 

(1,1)=(1,2)=(1,3)

(2,1)=(2,2)=(2,3)

(3,1)=(3,2)=(3,3)

Vertically:

(1,1) = (2,1) = (3,1)

(1,2) = (2,2) = (3,2)

(1,3) = (2,3) = (3,3)

Diagonally:

(1,1) = (2,2) = (3,3)

(1,3) = (2,2) = (3,1)

* Create an if/elif case for each and *if they’re satisfied, set gameover=True* and then at the end *if gameover is True, print(%s Wins!) %player letter*
* At the end of the function, **return gameover**

## STEP 6: Check for a tie
* **Create a function called tie_game that should take gameover and the gameboard**
* A draw means that neither player has 3 in a row, but there aren’t any empty squares (or ‘-’ in our case)
* ***So check that our gameboard has no ‘-’ in it***
* For each list in the outer list, **filter out the values that == ‘-’ and if the length of our remaining list isn’t 3 (that means there are hyphens in the list), we don’t have a tie, and we should return gameover(which starts at False)**

## STEP 7: Check if game over**
* Create a function called *check_game_over* 
* We will first call three_in_a_row on 'X' to see if gameover is set to true, if it isn't, we will call three_in_a_row on 'O' to see if this changes gameover. If neither of these change gameover to true, then we might have a tie so we call tie_game
* We add check_game_over() to the end of our while loop, and it should update our "gameover" condition if needbe


## STEP 8: If you haven’t already, wrap it up in a function!
* Just like with Hangman! 
* Remember to call tic_tac_toe() at the end of the while loop
* Play with someone :)

