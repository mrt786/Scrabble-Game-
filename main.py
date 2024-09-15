# Add the implementation logic code here
from turtle import Screen , Turtle
from screen import scrabbleScreen
from playsound import playsound
import threading

def play_background_music():
    audio_file_path = 'scrabbleSound.mp3'
    playsound(audio_file_path)

music_thread = threading.Thread(target=play_background_music)
music_thread.start()


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
s1 = scrabbleScreen(5) # passing the number of players
turtle.tracer(0)
s1.setScreen(screenHeight, screenWidth ,t1,gameScreen)
turtle.update()
gameScreen.onscreenclick(s1.clikcOnScreen)
turtle.mainloop()