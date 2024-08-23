from turtle import Turtle 
ALINGMENT = 'center'
FONT = ('Arial', 24, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("C:/Users/DELL/Desktop/python-projects/snake-game/data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score : {self.score} High Score:{self.high_score}", move=False, align=ALINGMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("C:/Users/DELL/Desktop/python-projects/snake-game/data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_score()



    def increase_score(self):
        self.score += 1
        self.update_score()

    