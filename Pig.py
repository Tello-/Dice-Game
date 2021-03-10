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

class TurnData:
    def __init__(self):
        print("Turn Data created")

class Turn:
    def __init__(self, playerNumber):
        print("Turn created for player %d" %playerNumber)
        self.playerNumber = playerNumber                        # Who's turn
        self.totalTurnRolls = 0                                 # How many rolls this turn
        self.rollSum = 0                                        # Turn point sum
        self.currentRollVal = 0                                 # Most recent roll
        self.firstRoll = True                                   # Flags first roll
        self.die = Dice()                                       # Die used for turn


    def turnPrompt(self):
        print("Player %d, it is your turn!" %self.playerNumber)
        

    def recordRoll(self, val:int):
        self.totalTurnRolls += 1
        self.currentRollVal = val
        self.rollSum += self.currentRollVal

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
            print("game running")
            
   

   #---------------------------------------------------------------------#
                        # DEBUG AREA #
   #---------------------------------------------------------------------#
