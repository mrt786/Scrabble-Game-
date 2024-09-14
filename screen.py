# from main import screenHeight, screenWidth ,t1
from graphics import Grid
from player import player
from squares import Square
from math import floor
from turtle import Turtle, Screen
import random
from data import game_data

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
        # work as a temporary  and stores the values to 4 directions 
        self.presentOnGrid ={
            "left":  "",
            "right": "",
            "top": "",
            "bottom":"", 
        }
        self.playersGotiOnGrid = {

        }
        self.temp = '0' # it will serve as temporary when the click is happend then something will be store while when it is pasted on the grid it will again become empty

    def createButtons(self,turtle,screenHeight,screenWidth):
        self.g1.createGrid(turtle,screenWidth, screenHeight,15) 
        turtle.penup()
        turtle.goto(60,-(screenHeight)/2.5)
        self.buttons["submit"] = [turtle.xcor(),turtle.ycor()]
        Square(turtle,80,40,turtle.xcor(),turtle.ycor(),"Submit")
        
    def setScreen(self,screenHeight, screenWidth ,t1,screenObject):
        for i in range(0,self.numberOfPlayers):
            self.playersGotiOnGrid[i] = [] # an empty list to store the contents playerwise that it pasted on the grid 
            p1 = player(t1,screenHeight,screenObject)
            if i == 0:
                p1.setPlayer(t1,60, (screenHeight)/2.5,screenWidth,screenHeight)
            else:
                p1.setPlayer(t1,60, t1.ycor() - 20,screenWidth,screenHeight)
            self.gamePlayers.append(p1) # it willl append the players in the players array
            self.playersGotiOnGrid[p1.playerKey] = []
        self.createButtons(t1,screenHeight,screenWidth)

    def submitButton(self):
        print("submit is working")
        if self.move % self.numberOfPlayers == 0:
            self.move = 1
        else:
            self.move += 1

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

    #     # bottom
        for i in range(x,-1,-1):
            if self.g1.tiles[i][y][2] == " ":
                return
            else:

                self.presentOnGrid["bottom"] += str(self.g1.tiles[i][y][2])  
    
    # store the words all direction to the words that is recently added
    def storeWords(self, x , y):

        for key in self.presentOnGrid:
            self.presentOnGrid[key] = ""
        self.storeLeft(x,y)
        self.storeRight( x , y)
        self.storeTop( x , y)
        self.storeBottom(x , y)

        # search the word in the data
    
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
                self.temp = '0'
                return True
        return False

                # call a function that stores left , right, top, bottom of the word

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

    def clikcOnScreen(self,x,y):
        # when the player clicks on the submit button
        if (x >= self.buttons["submit"][0] and x <= self.buttons["submit"][0] + 80 )  and (y >= self.buttons["submit"][1] and y <= self.buttons["submit"][1] + 40 ):
            self.submitButton()
        
        # when it clicks on the grid to paste the goti 
        elif x >= int(self.g1.tiles[0][0][0]) and x <= abs(int(self.g1.tiles[0][14][0]) ) and y >= int(self.g1.tiles[0][0][1]) and y <= abs(int(self.g1.tiles[0][14][1])): #and (y >= -620 and y <= 620):
            print("click on the grid", x, y)

            # here my xindex represents y and yindex represents x
            yIndex = floor((x)/self.g1.boxWidth) + 15
            xIndex = floor((y + (self.g1.boxHeight/2))/self.g1.boxHeight) + 7


            if(self.checkSquareIsEmpty(xIndex,yIndex)):
                self.storeWords(xIndex,yIndex)


        #when it clicks on the tiles of player   
        else:
            if self.temp == '0':
                count = 0
                for i in self.gamePlayers[self.move-1].playerGotianCollection:
                    if (x <= i[0] and x >= i[0] - self.gamePlayers[self.move-1].playerGotiSize) and (y >= i[1] and y <= i[1] + self.gamePlayers[self.move-1].playerGotiSize):#and self.gamePlayers[self.move-1].present:
                        if i[3] == True:
                            self.temp = i[2] # copy the key of the
                            # draw empty square on the box
                            self.drawEmptySquare(i[0],i[1],'black')
                            i[3] =  False  
                            print ("Character is selected")
                            self.playersGotiOnGrid[self.move-1].append(count)
                            if self.temp == '-':
                                s1 = Screen()
                                self.temp = s1.textinput("temp","Enter goti of your choice. If you entered an invalid goti you will be penalized.Sytem will automatically select a goti")
                                self.temp = self.temp.lower()
                                if not(ord(self.temp) >= 97 and ord(self.temp) <= 122):
                                    self.temp  = chr(random.randint(97,122))
                                    
                    count += 1 
                    
    