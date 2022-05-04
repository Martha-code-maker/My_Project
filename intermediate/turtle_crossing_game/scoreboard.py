from turtle import Turtle

FONT = ("Courier", 20, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 1
        self.update_level()


    def update_level(self):
        self.clear()
        self.goto(-280,260)
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def level_up(self):
        self.level += 1
        self.update_level()

    def collision_detect(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=FONT)

