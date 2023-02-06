from turtle import Turtle

class Ball(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.pu()
        self.move_forward_y=10
        self.move_forward_x=10
        self.move_speed=0.1
    
    def move(self):
        new_x=self.xcor()+self.move_forward_x
        new_y=self.ycor()+self.move_forward_y
        self.goto(x=new_x,y=new_y)
    
    def collision_y(self):
        self.move_forward_y*=-1
    
    def collision_x(self):
        self.move_forward_x*=-1
        self.move_speed*=0.9
    
    def reset_position(self):
        self.goto(0,0)
        self.move_speed=0.1
        self.move_forward_x*=-1