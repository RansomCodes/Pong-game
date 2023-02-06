from turtle import Turtle

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color("white")
        self.pu()
        self.hideturtle()
        self.l_score=0
        self.r_score=0
        self.score_print()
    
    def score_print(self):
        self.clear()
        self.goto(-100,190)
        self.write(self.l_score,align="center",font=("Courier",80,"normal"))
        self.goto(100,190)
        self.write(self.r_score,align="center",font=("Courier",80,"normal"))
        
    def l_point(self):
        self.l_score+=1
        self.score_print()
    
    def r_point(self):
        self.r_score+=1
        self.score_print()