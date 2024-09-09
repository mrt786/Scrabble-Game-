import random
light_colors = [
    "Light Blue",
    "Light Coral",
    "Light Goldenrod Yellow",
    "Light Gray",
    "Light Green",
    "Light Pink",
    "Light Salmon",
    "Light Sea Green",
    "Light Sky Blue",
    "Light Slate Gray",
    "Light Steel Blue",
    "Light Yellow"
]

class Square:
    def drawSquare(self, turtle):
        turtle.speed(0)
        turtle.fillcolor(self.color)
        turtle.begin_fill()
        turtle.forward((self.length))
        turtle.left(90)
        turtle.forward(self.height)
        turtle.left(90)
        turtle.forward((self.length))
        turtle.left(90)
        turtle.forward(self.height)
        turtle.left(90)
        turtle.forward((self.length))
        turtle.end_fill()
        turtle.penup()
        turtle.goto(turtle.xcor() - self.length/2,turtle.ycor() + self.height/4)
        turtle.write(self.insideValue, align="center", font=("Arial",int(self.length/2), "bold"))
        turtle.goto(turtle.xcor() + self.length/2,turtle.ycor() - self.height/4)
        turtle.pendown()
    

    def __init__(self,turtle,Length, Height, Xcor, Ycor, key):
        self.length = Length
        self.height = Height
        self.color = random.choice(light_colors)
        self.xcor = Xcor
        self.ycor = Ycor
        self.insideValue = key
        self.drawSquare(turtle)
    
    