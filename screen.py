# from main import screenHeight, screenWidth ,t1
from graphics import Grid
from player import player
from squares import Square
from math import floor
from turtle import Turtle, Screen
import random
from data import game_data
import json
import os
class scrabbleScreen:
    def __init__(self,nPlayers):
        self.numberOfPlayers = nPlayers
        self.g1 = Grid()
        self.move = 1
        self.gamePlayers = []
        self.buttons = {
            "submit":[],
            "finish":[]
        }
        # storing the given data as  dictionaries
        wordsArray = {}
        self.checksArray = []
        for word in game_data["words"]:
            firstCharacter = word[0].lower()

            if firstCharacter not in wordsArray:
                wordsArray[firstCharacter] = []
            wordsArray[firstCharacter].append(word.lower())
        del game_data["words"]
        game_data["words"] = wordsArray
        del wordsArray
        self.outputOnScrabble = []
        # work as a temporary  and stores the values to 4 directions 
        self.presentOnGrid ={
            "left":  "",
            "right": "",
            "top": "",
            "bottom":"", 
        }
        self.playersGotiOnGrid = {

        }
        self.indexOfCharactersOnGrid = []
        self.tempIndexOfCharactersOnGrid = [] # it will store the indexes
        self.temp = '0' # it will serve as temporary when the click is happend then something will be store while when it is pasted on the grid it will again become empty
        self.gotianAddedByplayerOnGrid = ""
        self.foundedWords = []
        self.tempWords = []
        self.totalMoves = 1
        self.playerCreatedWords = []
    def calculateScore(self, gotian):
        score = 0
        for goti in gotian:
            for item in game_data["alphabet_score"]:
                if item["alphabet"] ==  goti:
                    score += item["score"]
                    break
        return score

    def storeWordToJson(self,word):
        playerFileName = f'players/{self.gamePlayers[self.move-1].playerName}.json'
        playerDir = os.path.dirname(playerFileName)

        if not os.path.exists(playerDir):
            os.makedirs(playerDir)

        if os.path.exists(playerFileName):
            with open(playerFileName, 'r') as file:
                player_data = json.load(file)
        else:
            player_data = {}

        player_data[word] = self.calculateScore(word)

        with open(playerFileName, 'w') as file:
            json.dump(player_data, file, indent=4)
        
    def StoreWordToWinner(self):
        Score = 0
        winner = None
        for player_file in os.listdir('players/'):
            if player_file.endswith('.json'):
                with open(os.path.join('players/', player_file), 'r') as file:
                    player_data = json.load(file)
                
                total_score = sum(player_data.values())
                if total_score > Score:
                    Score = total_score
                    winner = {
                        'name': player_file.split('.')[0],
                        'words': player_data
                    }

        if winner:
            with open('winner.txt', 'a') as file:
                file.write(f"Player: {winner['name']}\n")
                for word, score in winner['words'].items():
                    file.write(f"{word}: {score}\n")
            print(f"Winner is {winner['name']} with total score {Score}")

    def createButtons(self,turtle,screenHeight,screenWidth):
        self.g1.createGrid(turtle,screenWidth, screenHeight,15) 
        turtle.penup()
        turtle.goto(60,(screenHeight)/2.5 + 50)
        self.buttons["submit"] = [turtle.xcor(),turtle.ycor()]
        Square(turtle,80,40,turtle.xcor(),turtle.ycor(),"Submit")
        
        self.g1.createGrid(turtle,screenWidth, screenHeight,15) 
        turtle.penup()
        turtle.goto(150,(screenHeight)/2.5 + 50)
        self.buttons["Hint"] = [turtle.xcor(),turtle.ycor()]
        Square(turtle,80,40,turtle.xcor(),turtle.ycor(),"Hint")
    
    def drawEmptySquare(self,x,y,color):
            # after clicking on the player goti collection an empty square will be drawn on the square it is clicked
            t1 = Turtle()
            t1.penup()
            t1.goto(x - self.gamePlayers[self.move-1].playerGotiSize,y)
            t1.fillcolor(color)
            t1.begin_fill()
            t1.forward((self.gamePlayers[0].playerGotiSize ))
            t1.left(90)
            t1.forward(self.gamePlayers[0].playerGotiSize )
            t1.left(90)
            t1.forward((self.gamePlayers[0].playerGotiSize ))
            t1.left(90)
            t1.forward(self.gamePlayers[0].playerGotiSize )
            t1.left(90)
            t1.forward((self.gamePlayers[0].playerGotiSize ))
            t1.end_fill()   
    
    def setScreen(self,screenHeight, screenWidth ,t1,screenObject):
    # def __init__(self,turtle,Length, Height, Xcor, Ycor, key):
        t1.goto(-605,297)
        Square(t1,600,40,0,0,"Welcome To Scrabble")
        self.outputOnScrabble = [-605,297]
        for i in range(0,self.numberOfPlayers):
            self.playersGotiOnGrid[i] = [] # an empty list to store the contents playerwise that it pasted on the grid 
            p1 = player(t1,screenHeight,screenObject)
            if i == 0:
                p1.setPlayer(t1,60, (screenHeight)/2.5,screenWidth,screenHeight)
            else:
                p1.setPlayer(t1,60, t1.ycor() - 20,screenWidth,screenHeight)
            self.gamePlayers.append(p1) # it willl append the players in the players array
        self.createButtons(t1,screenHeight,screenWidth)

    def emptyPresentOnGrid(self):
        for key in self.presentOnGrid:
            self.presentOnGrid[key] = ""

    #search words from the data
    def increaseScore(self,gotian):
        print(gotian)
        for goti in gotian:
            for item in game_data["alphabet_score"]:
                if item["alphabet"] ==  goti:
                    self.gamePlayers[self.move-1].playerScore  += item["score"]
                    break 
        t1 = Turtle()
        t1.color("white")
        t1.penup()
        t1.goto(self.gamePlayers[self.move-1].playerScorePosition[0],self.gamePlayers[self.move-1].playerScorePosition[1])
        self.gamePlayers[self.move-1].drawSquare(t1,140,20)
        t1.goto(t1.xcor() - 130 , t1.ycor())
        t1.write(self.gamePlayers[self.move-1].playerScore, align="center", font=("Arial",10, "bold"))
        self.emptyPresentOnGrid()
        t1.color('black')

    def wordSearch(self,wordFromGrid,wordFromData ):
        # if len(wordFromGrid) == 1:
        #     return False
        # exactly match
        if wordFromData in wordFromGrid:
            self.foundedWords.append(wordFromData)
            self.playerCreatedWords.append(wordFromData)
            return True
        # if the word is matched partially
        elif wordFromGrid in wordFromData:
            return True
        # if the word is not matched partially or completely
        return False
    
    def storeLeft(self,x,y):
        #left
        for i in range(y,-1,-1):
            if self.g1.tiles[x][i][2] == " ":
                return
            else:
                self.presentOnGrid["left"] = str(self.g1.tiles[x][i][2]) + self.presentOnGrid["left"]
    
    def storeRight(self,x,y):
        # right
        for i in range(y,15):
            if self.g1.tiles[x][i][2] == " ":
                return
            else:

                self.presentOnGrid["right"] += str(self.g1.tiles[x][i][2])
    
    def storeTop(self,x,y):
        # top
        for i in range(x,15):
            if self.g1.tiles[i][y][2] == " ":
                return
            else:
                self.presentOnGrid["top"] = str(self.g1.tiles[i][y][2]) + self.presentOnGrid["top"] 

    def storeBottom(self,x,y):
        for i in range(x ,-1,-1):
            if self.g1.tiles[i][y][2] == " ":
                return
            else:
                self.presentOnGrid["bottom"] += str(self.g1.tiles[i][y][2])  
    

    # store the words all direction to the words that is recently added
    def storeWords(self, x , y):
        self.storeLeft(x,y)
        self.storeRight( x , y)
        self.storeTop( x , y)
        self.storeBottom(x , y)

    def Hint(self):
        temp = ""

    #     for i in range(0,15):
    #         for j in range(0,15):
    #             if self.g1.tiles[i][j] == " ":

    #             else:
    #                 temp += self.g1.tiles[i][j]

    def discardWords(self):
        # first of all store in the ascending order
        self.tempWords = sorted(self.tempWords, key=len)
        self.tempWords = [word for word in self.tempWords if len(word) > 1]

    def gameEnd(self):
        score = 0
        name = ""
        for player in self.gamePlayers:
            if player.playerScore > score:
                score = player.playerScore
                name = player.playerName
        t1 = Turtle()
        t1.penup()
        t1.goto(self.outputOnScrabble[0],self.outputOnScrabble[1])
        Square(t1,600,40,0,0,f"Congratulaions {name} You Won")
        self.StoreWordToWinner()

    def submitButton(self):
        if self.temp == '0':
            self.indexOfCharactersOnGrid = sorted(self.indexOfCharactersOnGrid, key=lambda item: (item[0], -item[1]))
            self.tempIndexOfCharactersOnGrid = list(self.indexOfCharactersOnGrid)
            
            for i in self.indexOfCharactersOnGrid[:]:
                # for right 
                x, y = i
                left= (y < 14 and self.g1.tiles[x][y + 1][2] != ' ' )
                if  left:
                    self.indexOfCharactersOnGrid.remove(i)
    
            for i in self.indexOfCharactersOnGrid[:]:
                # for top and bottom
                x, y = i
                top= ( x < 14 and self.g1.tiles[x+1][y][2] != ' ' )
                if  top:
                    self.indexOfCharactersOnGrid.remove(i)

            for i in self.indexOfCharactersOnGrid:
                self.storeWords(i[0],i[1])
                if (len(self.presentOnGrid["right"]) > 0) and (len(self.presentOnGrid["left"]) > 0)  and self.presentOnGrid["left"][-1]  ==  self.presentOnGrid["right"][0]:
                    self.presentOnGrid["right"] = self.presentOnGrid["right"][1:]
                
                self.tempWords.append(self.presentOnGrid["left"] + self.presentOnGrid["right"])
                if (len(self.presentOnGrid["top"]) > 0) and (len(self.presentOnGrid["bottom"]) > 0)   and  self.presentOnGrid["top"][-1]  ==  self.presentOnGrid["bottom"][0] :
                    self.presentOnGrid["bottom"] = self.presentOnGrid["bottom"][1:]
                self.tempWords.append(self.presentOnGrid["top"] + self.presentOnGrid["bottom"])
                self.emptyPresentOnGrid()
            self.discardWords()
            self.checksArray = []
            
            for word in self.tempWords:
                tempCheckArray = []
                for dataWord in game_data["words"][word[0]]:
                    tempCheckArray.append(self.wordSearch(word,dataWord))
                if any(tempCheckArray):
                    self.checksArray.append(True)
                else:
                    self.checksArray.append(False)
            if not(any(self.checksArray)):# if there is a single word that is not found
                self.gamePlayers[self.move-1].returnGoti(self.playersGotiOnGrid[self.move-1])
                self.g1.returnGoti(self.tempIndexOfCharactersOnGrid)
            else:
                self.gamePlayers[self.move-1].reDrawGoti(self.playersGotiOnGrid[self.move-1])  
                self.increaseScore(self.gamePlayers[self.move-1].playerGotianInserted)
                self.playerCreatedWords = list(set(self.playerCreatedWords))
                for word in self.playerCreatedWords:
                    self.storeWordToJson(word)
            
            self.playerCreatedWords = []
            self.indexOfCharactersOnGrid = []

            self.playersGotiOnGrid[self.move-1].clear()
            self.tempWords.clear()
            self.gamePlayers[self.move-1].playerGotianInserted = ""
            if self.move % self.numberOfPlayers == 0:
                self.move = 1
            else:
                self.move += 1
            self.totalMoves += 1
            if self.totalMoves / self.gamePlayers[self.move -1].numOfPlayer  == 5:
                self.gameEnd()
    def checkSquareIsEmpty(self,x,y):

        if  (x >= 0 and x <= 14 ) and ( y >= 0 and y <= 14):
            # to check whether the box on the grid where it is clicked is empty or not
            if(self.g1.tiles[x][y][2] == " " and self.temp != '0'):
                turtle = Turtle() 
                turtle.penup()
                turtle.color("black")
                turtle.goto(self.g1.tiles[x][y][0],self.g1.tiles[x][y][1])
                turtle.goto(turtle.xcor() + self.g1.boxWidth/2,turtle.ycor() + self.g1.boxHeight/4)
                turtle.write(self.temp, align="center", font=("Arial",15, "bold"))
                turtle.goto(turtle.xcor() - self.g1.boxWidth/2,turtle.ycor() - self.g1.boxHeight/4)
                self.g1.tiles[x][y][2] = self.temp
                self.gamePlayers[self.move-1].playerGotianInserted += self.temp
                self.temp = '0'
                return True
        return False

                # call a function that stores left , right, top, bottom of the word
       

    def clikcOnScreen(self,x,y):
        # when the player clicks on the submit button
        if (x >= self.buttons["submit"][0] and x <= self.buttons["submit"][0] + 80 )  and (y >= self.buttons["submit"][1] and y <= self.buttons["submit"][1] + 40 ):
            self.submitButton()

        elif (x >= self.buttons["Hint"][0] and x <= self.buttons["Hint"][0] + 80 )  and (y >= self.buttons["Hint"][1] and y <= self.buttons["Hint"][1] + 40 ):
            self.Hint()
        # when it clicks on the grid to paste the goti 
        elif x >= int(self.g1.tiles[0][0][0]) and x <= abs(int(self.g1.tiles[0][14][0]) ) and y >= int(self.g1.tiles[0][0][1]) and y <= abs(int(self.g1.tiles[0][14][1])): #and (y >= -620 and y <= 620):

            # here my xindex represents y and yindex represents x
            yIndex = floor((x)/self.g1.boxWidth) + 15
            xIndex = floor((y + (self.g1.boxHeight/2))/self.g1.boxHeight) + 7


            if(self.checkSquareIsEmpty(xIndex,yIndex)):
                self.indexOfCharactersOnGrid.append([xIndex,yIndex])

        #when it clicks on the tiles of player   
        else:
            if self.temp == '0':
                count = 0
                for i in self.gamePlayers[self.move-1].playerGotianCollection:
                    if (x <= i[0] and x >= i[0] - self.gamePlayers[self.move-1].playerGotiSize) and (y >= i[1] and y <= i[1] + self.gamePlayers[self.move-1].playerGotiSize):#
                        if i[3] == True:
                            self.temp = i[2] # copy the key of the
                            # draw empty square on the box
                            self.drawEmptySquare(i[0],i[1],'black')
                            i[3] =  False  
                            self.playersGotiOnGrid[self.move-1].append(count)
                            self.gotianAddedByplayerOnGrid += self.temp
                            if self.temp == '-':
                                s1 = Screen()
                                self.temp = s1.textinput("temp","Enter goti of your choice. If you entered an invalid goti you will be penalized.Sytem will automatically select a goti")
                                self.temp = self.temp.lower()
                                if not(ord(self.temp) >= 97 and ord(self.temp) <= 122):
                                    self.temp  = chr(random.randint(97,122))   
                    count += 1 
                    
    