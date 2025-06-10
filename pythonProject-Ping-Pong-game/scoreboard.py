from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-200, 200)
        self.write(arg=self.l_score, move=False, align="center", font=("Courier", 50, "bold"))
        self.goto(200, 200)
        self.write(arg=self.r_score, move=False, align="center", font=("Courier", 50, "bold"))

    def l_point(self):
        self.l_score +=1
        self.update_scoreboard()

    def r_point(self):
        self.r_score +=1
        self.update_scoreboard()

    def game_over(self):
        self.home()
        self.write(arg="GAME OVER", move=False, align="center", font=("Courier", 50, "bold"))



