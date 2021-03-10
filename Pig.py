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
        self.playerNumber = playerNumber
        self.totalTurnRolls = 0
        self.rollSum = 0
        self.currentRollVal = 0
        self.firstRoll = True
        self.die = Dice()


    def turnPrompt(self):
        print("Player %d, it is your turn!" %self.playerNumber)
        

    def addRoll(self, val:int):
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
        self.humanPlayers = list(())

        for x in range(self.numHumanPlayers):
            self.humanPlayers.append(Player(x+1))


    def printStats(self, playerNumber:int):    
        if playerNumber>0 and playerNumber<(self.numHumanPlayers + self.numBotPlayers)
            print("-----------------------------")
            print("Player # %d" %.number)
            print("Career Rolls: %d" %y.numGameRolls)
            print("Score: %d" %y.score)
            print("-----------------------------")

    def printStats(self):    
        for y in self.humanPlayers:
            print("-----------------------------")
            print("Player # %d" %y.number)
            print("Career Rolls: %d" %y.numGameRolls)
            print("Score: %d" %y.score)
            print("-----------------------------")

    def run(self):
        while(True):
            print("game running")
            
   

   #---------------------------------------------------------------------#
                        # DEBUG AREA #
   #---------------------------------------------------------------------#
