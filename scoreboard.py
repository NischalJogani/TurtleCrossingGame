from turtle import Turtle

FONT1 = ("Courier", 24, "normal")
FONT2 = ("Courier", 18, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 1
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(-200, 200)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.score}", align="center", font=FONT2)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=FONT1)
