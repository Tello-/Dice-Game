# Dice-Game
Project for CPSC 386 : Game Design


# Dice Game 
### Due Mar 23 by 11:59pm Points 10
### Introduction
###
###
#The objectives of this exercise are

Verify that a student's development environment is set up
Refresh our memory on how to write a program to a specification
Improving our programming practices
Learn about the Python programming language and it's standard library
We shall all write the dice game named Pig (Links to an external site.). Pig is a game that is probably quite old and was first described in print by John Scarne (famous for Scarne's four aces trick (Links to an external site.)).

The game uses only one six sided die and is played with 2 or more players. Players take turns rolling the die and tabulating a score according to the rules. The first player to score 100 or more points wins.

In our version of the game, the six-sided die will be simulated by the computer. Additionally, the game can be played against the computer should there only be one player. If there is more than one player, the game is played as a hotseat (Links to an external site.) multiplayer game.

# Rules
There is at least two players playing the game. A two player game may be against another player or against the computer. Three or more player games do not have a computer player to play against.
There is at most 4 players in a game.
There is one six-sided die (simulated by the game using a psuedo-random number generator); the faces of the die are numbered 1, 2, 3, 4, 5, and 6. Opposing sides of the die sum to 7 (standard western casino dice).
The game is turn based. The player who goes first is selected by each player rolling the die once. The players are ordered from in ascending order. If there is a tie between two or more players, the computer can break the tie by arbitrarily assigning that player to a position not less than the position the player rolled.
Once each player has had a turn in ascending order, the turn returns to the first player.
Each turn, a player rolls the die.
If the player rolls a 1, the player scores nothing that turn and it becomes the next player's turn. The player's overall score does not change because the player has lost the points accrued during their turn.
If the player rolls any other number, the value of the die is added to their turn's score as points and the player's turn may continue. The player's overall score does not change until their turn ends.
If a player chooses to hold, their turn total is added to their score, and it becomes the next player's turn.
The play may not choose to hold until after the die has been rolled at least once.
The game ends when a player ends their turn with a score of 100 points or greater.
At the beginning of every die roll, the game displays the current player's total score, current turn score, and how many times the player has rolled. Once the die is rolled, the computer displays the value of the die. If it is a 1, the computer ends the current player's turn and moves on to the next player.
 # Requirements

In the file README.md, identify who you are and what game you wrote. Write a brief synopsis of the game and summarize the rules. Provide an example of game play. Document any features or details you believe makes your game stand out.

The game must be written in Python 3. Limit your game to use only what is available in the Python Standard Library (Links to an external site.). Do not use additional Python modules that are outside of the Python Standard Library.

The user interface of the game is text. There are no graphics (2D, 3D, sprites, etc.) in this game. If you would like to use audio effects or a soundtrack, you may however the program may only use what's available in the Python Standard Library.

The computer player does not need to be a sophisticated machine. You may make the computer player as simple or as sophisticated as you like. However, the computer player should not appear to be unpredictable.

The game should take advantage of object oriented design. To the best of your ability, attempt to model elements of the game as objects. Some elements of the game that can naturally map onto an object are the die, the player, and the computer player.

Since this game is a terminal based game, use sleep (Links to an external site.) to slow down the game to make the text appear on the screen slowly. Give the player an opportunity to read the text. Students are encouraged to use curses in lieu of graphics.
