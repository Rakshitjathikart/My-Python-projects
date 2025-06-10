from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.color("white")
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(arg=f"score:{self.score}", move=False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.color("red")
        self.goto(0,0)
        self.write(arg="GAME OVER", move=False, align=ALIGNMENT, font=FONT)

    def inc_score(self):
        self.score += 1
        self.update_score()







