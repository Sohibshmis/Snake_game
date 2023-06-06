from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 20, 'bold')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()
        self.hideturtle()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!", align=ALIGNMENT, font=FONT)
        self.color("cyan")
        self.goto(0, -20)
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=('Courier', 14, 'bold'))

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score:{self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        if self.score % 5 == 0:
            self.score += 2
        self.update_scoreboard()


