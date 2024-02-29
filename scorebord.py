from turtle import Turtle
ALIGNMENT_R = "right"
ALIGNMENT_L = "left"
FONT = ("courier", 60, "normal")


class Scorebord(Turtle):
    def __init__(self):
        super().__init__()
        self.r_score = 0
        self.l_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.r_paddle_score()
        self.l_paddle_score()

    def r_paddle_score(self):
        self.goto(150, 200)
        self.write(f"{self.r_score}", align=ALIGNMENT_R, font=FONT)

    def l_paddle_score(self):
        self.goto(-100, 200)
        self.write(f"{self.l_score}", align=ALIGNMENT_R, font=FONT)

    def increase_r_score(self):
        self.r_score += 1
        self.clear()
        self.r_paddle_score()

    def increase_l_score(self):
        self.l_score += 1
        self.clear()
        self.l_paddle_score()