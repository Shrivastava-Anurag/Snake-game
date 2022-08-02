from turtle import Turtle



class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as score:
            self.highscore = int(score.read())
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 265)
        self.update_scoreboard()


    def update_scoreboard(self):
       self.clear()
       self.write(f"Score: {self.score} | HighScore: {self.highscore}", align="center", font=("Arial", 24, "normal"))

    def score_increment(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", mode="w") as score:
                score.write(str(self.highscore))
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.color("white")
    #     self.write("Game Over", align="center", font=("Arial", 24, "normal"))