# Add the implementation logic code here
from turtle import Screen , Turtle
from graphics import Grid
from player import *
t1 = Turtle()

gameScreen = Screen()
gameScreen.bgcolor("black")
t1.hideturtle()
t1.color("black")
screenWidth = 1250
screenHeight = 700
gameScreen.setup(width=screenWidth,height=screenHeight)
screenWidth = screenWidth - 40 
screenHeight = screenHeight - 80
gameScreen.title("Scrabble Game")
g1 = Grid()
# g1.createGrid(t1,screenWidth, screenHeight,15) 

t1.penup()
# t1.goto(20 , (screenHeight)/2.5)
t1.pendown()

# (self,Name, numberOfGotian,GotiSize,turtle,xcor , ycor,screenWidth, screenHeight) constructor parameters
p1 = player("Rehan",20 , 40 ,t1,60, (screenHeight)/2.5,screenWidth,screenHeight)
p2 = player("Musa",10 , 40 ,t1,60, t1.ycor() - 20,screenWidth,screenHeight)
p3 = player("Hashim",10 , 40 ,t1,60, t1.ycor() - 20,screenWidth,screenHeight)
gameScreen.exitonclick()