# Add the implementation logic code here
from turtle import Screen , Turtle
from screen import scrabbleScreen
import turtle
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
s1 = scrabbleScreen(1) # passing the number of players
turtle.tracer(0)
s1.setScreen(screenHeight, screenWidth ,t1,gameScreen)
turtle.update()
gameScreen.onscreenclick(s1.clikcOnScreen)
turtle.mainloop()