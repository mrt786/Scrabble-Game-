from data import game_data
import random
from squares import *
class player:
    numOfPlayer = 0 # class level object
    # sizeOfGoti = int(input("Enter the goti size: "))
    sizeOfGoti = 40
    def __init__(self,turtle,screenHeight,screenObject):
        if turtle.ycor() < -(screenHeight/2):
            # implement the functionality if the Players information is filled
            return
        # data members for the player
        # self.playerName = screenObject.textinput("name","Enter the name of the Player: ")
        self.playerName  = "rehan"
        self.playerScore = 0 
        self.totalGotian = 20
        self.presentGotian = 0
        self.playerGotianCollection = [] #it contians n number of gotian
        self.playerGotiSize = player.sizeOfGoti
        player.numOfPlayer += 1
        self.playerKey = self.numOfPlayer # this will save a unique key for the player


    def setPlayer(self,turtle,xcor , ycor,screenWidth, screenHeight):
        # display the name and the score of the player
        turtle.penup()
        turtle.color("white")
        turtle.goto(xcor, ycor)
        turtle.write(f"{self.playerName} Score = 0", align="center", font=("Arial",10, "bold"))
        turtle.goto(xcor ,ycor - self.playerGotiSize-10 )
        turtle.pendown()
        turtle.color("black")

        # implementation for the collection of the 
        for i in range(0,self.totalGotian):
            if turtle.xcor() > screenWidth/2:
                turtle.goto(xcor, turtle.ycor() - self.playerGotiSize)
            goti = random.choice(game_data["gotian"])# to select a random goti from the choice
            Square(turtle, self.playerGotiSize,self.playerGotiSize,turtle.xcor(),turtle.ycor(),goti)
            self.presentGotian = self.presentGotian + 1
            self.playerGotianCollection.append([turtle.xcor() , turtle.ycor(),goti,True])
        turtle.goto(xcor, turtle.ycor() - self.playerGotiSize/4)
        
