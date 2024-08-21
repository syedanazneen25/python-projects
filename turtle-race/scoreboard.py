from turtle import Turtle
FONT = ("courier", 24, "normal")

class Score(Turtle):
    def __init__(self):
        super().__init__() 
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.write(f"Level: {self.level}", align="left", font=FONT)
    def increase_level(self):
        self.level += 1
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)
    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"Game Over!!!", align="center", font=FONT)


