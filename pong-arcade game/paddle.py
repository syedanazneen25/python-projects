from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position) :
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.goto(position)
        self.shapesize(stretch_wid=5, stretch_len=1)

    
    def paddle_move_up(self):
        new_y = self.ycor() + 20
        self.sety(new_y)

    def paddle_move_down(self):
        new_y = self.ycor() - 20
        self.sety(new_y)