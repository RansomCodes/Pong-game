from turtle import Turtle

class Paddle(Turtle):
    
    def __init__(self,coordinates=()):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.pu()
        self.goto(coordinates)
    
    def moveup(self):
        new_y=self.ycor()+20
        self.goto(x=self.xcor(),y=new_y)
    
    def movedown(self):
        new_y=self.ycor()-20
        self.goto(x=self.xcor(),y=new_y)