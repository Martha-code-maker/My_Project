from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.score = 0
        with open('data.txt') as f:
            self.high_score = int(f.read())
        self.setposition(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score :{self.score} Highest Score: {self.high_score} ", False, align=ALIGNMENT, font=FONT)

    #def game_over(self):
    #    self.goto(0, 0)
    #    self.write(f"GAME OVER", False, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('data.txt',"w") as f:
                f.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()


    def add_score(self):
        self.score += 1
        self.update_scoreboard()











