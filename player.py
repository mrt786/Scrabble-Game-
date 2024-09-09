from data import game_data
import random
from squares import *
class player:
    def __init__(self,Name, numberOfGotian,GotiSize,turtle,xcor , ycor,screenWidth, screenHeight):
        if turtle.ycor() < -(screenHeight/2):
            # implement the functionality if the Players information is filled
            return
        
        # data members for the player
        self.playerName = Name
        self.playerScore = 0 
        self.totalGotian = numberOfGotian
        self.presentGotian = 0
        self.playerGotianCollection = [] #it contians n number of gotian
        self.playerGotiSize = GotiSize # it is the x i.e goti size length and width of the goti



        # display the name and the score of the player
        turtle.penup()
        turtle.color("white")
        turtle.goto(xcor, ycor)
        turtle.write(f"{Name} Score = 0", align="center", font=("Arial",10, "bold"))
        turtle.goto(xcor ,ycor - GotiSize -10 )
        turtle.pendown()
        turtle.color("black")

        # implementation for the collection of the 
        # 
        #  
        for i in range(0,numberOfGotian):
            # (self,turtle,Length, Height, Xcor, Ycor, key)
            if turtle.xcor() > screenWidth/2:
                turtle.goto(xcor, turtle.ycor() - GotiSize)
            playerGoti = Square(turtle, GotiSize,GotiSize,turtle.xcor(),turtle.ycor(),random.choice(game_data["gotian"]))
            self.presentGotian = self.presentGotian + 1
            self.playerGotianCollection.append([playerGoti])
        turtle.goto(xcor, turtle.ycor() - GotiSize/4)
        
