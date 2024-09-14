# Add the graphics (turtle) related code in this file
from squares import *
# this function is to draw the square
class Grid:
    #constructor for the class
    def __init__(self):
        self.x = 0
        self.y = 0
        self.size = 0 # size is the total number of the boxes in a row or column
        self.boxWidth = 0 
        self.boxHeight = 0
        self.tiles = []
    
    def createGrid(self,turtle,width , height,size):
        self.x = -(width/2) #screen left bottom cordinate
        self.y = -(height/2)
        self.size = size
        self.boxWidth = int((width)/(2*size)) # where the 2 is used for the half i.e the size of each square
        self.boxHeight = int((height)/size)
        #  to print the outer block
        turtle.penup()
        turtle.hideturtle()
        turtle.speed(0)
        turtle.goto(self.x,self.y)#left most corner
        turtle.pendown()
        list = []
        for i in range(0,size*size):
            if i != 0:
                if i % 15 == 0:  # as the grid size is fixed i.e 15
                    turtle.sety(int(turtle.ycor()) + self.boxHeight)
                    self.tiles.append(list)
                    turtle.setx(self.tiles[0][0][0])
                    list = []
            list.append([int(turtle.xcor()),int(turtle.ycor())," "])
            Square(turtle,self.boxWidth,self.boxHeight,turtle.xcor(),turtle.ycor()," ") #grid is empty
            # if(i/15 == 7):
            #     print(self.tiles)
            #     return
        self.tiles.append(list) 