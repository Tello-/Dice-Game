import random

TITLE = "Pig"
numPlayers = 1
currentPlayer = 1
turnBegin = True

class Player:
    def __init__(self, number:int, isBot:bool = False):
        print("Player %d Created" %number)
        self.number = number
        self.score = 0
        self.numGameRolls = 0
        self.isBot = isBot

class Dice:
    def __init__(self, sides = 6):
        print("%d sided die Created" %sides)
        self.sides = sides
    
    def roll(self):
        return random.randint(1,self.sides)


class Turn:
    def __init__(self, playerNumber):
        print("Turn created for player %d" %playerNumber)
        self.playerNumber = playerNumber                        # Who's turn
        self.totalTurnRolls = 0                                 # How many rolls this turn
        self.rollSum = 0                                        # Turn point sum
        self.prevRoll = 0                                       # Most recent roll
        self.firstRoll = True                                   # Flags first roll
        self.die = Dice()                                       # Die used for turn
        self.rolledOne = False                                  # Flag when 1 is rolled

    def turnPrompt(self):
        print("Player %d, it is your turn!" %self.playerNumber)

    def rollResult(self, result):
        print("You rolled %d" %result)
        
    def rollAgainPrompt(self) -> int:
        choice = int(0)
        while(int(choice) < 1) or (int(choice) > 2):
            choice = input("Would you like to (1)Roll Again? or (2)Bank your points? >> ")
        return choice

    def takeTurn(self) -> int:
        while True:
            self.turnPrompt()
            self.prevRoll = self.die.roll()
            self.rollResult(self.prevRoll)

            if(self.prevRoll == 1):
                print("No Points For You!")
                return 0
            else:
                print("You have accumulated some points")
                choice = self.rollAgainPrompt()
                if(choice == 1):
                    print("You want to roll again")

                elif(choice == 2):
                    print("You would like to bank your points.")







        return int() # TODO set return variable

    def recordRoll(self, val:int):
        self.totalTurnRolls += 1
        self.prevRoll = val
        self.rollSum += self.prevRoll

class Game:
    def __init__(self, humanPlayers:int = 1, botPlayers:int = 1, scoreGoal:int = 100):
        print("Game Created with %d human players, %d bot players and the score-to-win is %d" %(humanPlayers, botPlayers, scoreGoal))
        self.numHumanPlayers = humanPlayers
        self.numBotPlayers = botPlayers
        self.scoreGoal = scoreGoal
        self.currentTurn = Turn(1)
        self.players = list(())

        for x in range(0,self.numHumanPlayers):
            self.players.append(Player(x+1))

        for x in range(self.numHumanPlayers, self.numHumanPlayers + self.numBotPlayers):
            self.players.append(Player(x+1, True))



    def run(self):
        while(True):
            for ply in self.players:
                print(ply.number)
                thisTurn = Turn(ply.number)
                print("Player %d scored %d " %(ply.number, thisTurn.takeTurn()))
            print("Game finished, Goodbye")
            exit(0)
                
            
   

   #---------------------------------------------------------------------#
                        # DEBUG AREA #
   #---------------------------------------------------------------------#


mygame = Game(2,4,100)
mygame.run()