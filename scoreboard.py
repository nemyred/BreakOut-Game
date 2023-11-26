from turtle import Turtle

with open('high_score.txt') as file:
    high_score = file.read()


class ScoreBoard(Turtle):
    def __init__(self):
        self.score = 0
        self.level = 1
        self.lives = 3
        self.high_score = int(high_score)
        super().__init__()
        self.penup()
        self.hideturtle()
        self.setposition(500, -300)
        self.color('white')
        self.update_scoreboard()

    def update_score(self, number):
        self.score += number

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level {self.level}\nLives:{self.lives}\nScore: {self.score}\nHigh Score: {self.high_score}",
                   move=False, font=('Arial', 12, 'normal'))

    def game_over(self, status):
        self.clear()
        self.setposition(-275, 0)
        self.write(f"Game Over! You {status}! Your final score was {self.score}", move=False,
                   font=('Arial', 20, 'normal'))
        if self.high_score < self.score:
            # keep high score
            with open('high_score.txt', 'w') as high_file:
                high_file.write(f"{self.score}")

    def level_up(self):
        self.level += 1

    def lose_life(self):
        self.lives -= 1
