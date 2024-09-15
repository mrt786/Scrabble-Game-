from data import game_data
import random
from squares import *
from turtle import Turtle
from math import floor

class player:
    numOfPlayer = 0 # class level object
    playerGotianInserted = ""
    sizeOfGoti = 40
    def __init__(self,turtle,screenHeight,screenObject):
        if turtle.ycor() < -(screenHeight/2):
            # implement the functionality if the Players information is filled
            return
        # data members for the player
        self.playerName = screenObject.textinput("name","Enter the name of the Player: ")
        # self.playerName  = "rehan"
        self.playerScorePosition = []
        self.playerScore = 0 
        self.totalGotian = 28
        self.presentGotian = 0
        self.playerGotianCollection = [] #it contians n number of gotian
        self.playerGotiSize = player.sizeOfGoti
        player.numOfPlayer += 1
        self.playerKey = self.numOfPlayer # this will save a unique key for the player

    def drawSquare(self,turtle,lenght, height,color = "black"):
        turtle.fillcolor(color)
        turtle.begin_fill()
        turtle.forward((lenght))
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
        turtle.forward((lenght))
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
        turtle.forward((lenght))
        turtle.end_fill()

    def reDrawGoti(self,gotianRedraw):
        for i in gotianRedraw:
            t1 = Turtle()
            self.playerGotianCollection[i][2] = random.choice(game_data["gotian"])# to select a random goti from the choice
            self.playerGotianCollection[i][3] = True
            t1.penup()
            t1.goto(self.playerGotianCollection[i][0] - self.playerGotiSize,self.playerGotianCollection[i][1])
            t1.pendown()
            Square(t1, self.playerGotiSize,self.playerGotiSize,self.playerGotianCollection[i][0],self.playerGotianCollection[i][1],self.playerGotianCollection[i][2] )
    
    def returnGoti(self,gotianRedraw):
        
        for i in gotianRedraw:
            self.playerGotianCollection[i][3] = True
            t1 = Turtle()
            t1.penup()
            t1.goto(self.playerGotianCollection[i][0] - self.playerGotiSize,self.playerGotianCollection[i][1])
            t1.pendown()
            Square(t1, self.playerGotiSize,self.playerGotiSize,self.playerGotianCollection[i][0],self.playerGotianCollection[i][1],self.playerGotianCollection[i][2] )

    def setPlayer(self,turtle,xcor , ycor,screenWidth, screenHeight):
        # display the name and the score of the player
        turtle.penup()
        turtle.color("white")
        turtle.goto(xcor, ycor)
        self.drawSquare(turtle,140,20)
        turtle.goto(turtle.xcor() - 80, ycor)
        turtle.write(f"{self.playerName} Score =", align="center", font=("Arial",10, "bold"))
        turtle.goto(turtle.xcor() + 60 , ycor)
        self.drawSquare(turtle,140,20,)
        turtle.goto(turtle.xcor()-120, turtle.ycor())
        self.playerScorePosition = [turtle.xcor() -20,turtle.ycor()]
        turtle.write(f"{self.playerScore} ", align="center", font=("Arial",10, "bold"))
        turtle.goto(xcor ,ycor - self.playerGotiSize-10 )
        turtle.color("black")
        turtle.pendown()

        # implementation for the collection of the 
        
        for i in range(0,self.totalGotian):
            if turtle.xcor() > screenWidth/2:
                turtle.goto(xcor, turtle.ycor() - self.playerGotiSize)
            goti = random.choice(game_data["gotian"])# to select a random goti from the choice
            Square(turtle, self.playerGotiSize,self.playerGotiSize,turtle.xcor(),turtle.ycor(),goti)
            self.presentGotian = self.presentGotian + 1
            self.playerGotianCollection.append([turtle.xcor() , turtle.ycor(),goti,True])
        turtle.goto(xcor, turtle.ycor() - self.playerGotiSize/4)
        
