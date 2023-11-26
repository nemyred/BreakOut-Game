import time
import turtle
from bricks import Brick
from bat import Bat
from ball import Ball
from scoreboard import ScoreBoard

# keep score
#  mount scoreboard
scoreboard = ScoreBoard()
# set up Screen
screen = turtle.Screen()
screen.setup(600, 400)
screen.bgcolor("black")
screen.title("Breakout Game")
screen.listen()

# Create paddle
bat = Bat()

# Move paddle to user input
screen.onkey(bat.move_left, "Left")
screen.onkey(bat.move_right, "Right")
screen.onkeypress(bat.move_left, "Left")
screen.onkeypress(bat.move_right, "Right")
# Create ball
ball = Ball(-65)
brick = Brick()


# Create bricks with colour
def create_bricks():
    position_x = 550
    position_y = 300
    colour_list = ['blue', 'gray', 'purple', 'pink']
    colour_pick = -1

    for i in range(1, 97):
        colour = colour_list[colour_pick]
        brick.create_brick(position_x, position_y, colour)
        position_x -= 100
        if i % 12 == 0:
            position_y -= 50
            position_x = 550
        if i % 24 == 0:
            colour_pick += 1


create_bricks()


def outcome():
    # lose advice
    if scoreboard.lives == 0:
        for chosen_brick in brick.brick_list:
            chosen_brick.goto(1000, 10000)
        ball.goto(50000, 5000)
        bat.goto(5000, 1000)
        status = "lose"
        scoreboard.game_over(status)

    if scoreboard.level == 3 and brick.brick_list == []:
        bat.goto(5000, 1000)
        ball.goto(5000, 1000)
        status = 'win'
        scoreboard.game_over(status)

    if scoreboard.level < 3 and brick.brick_list == []:
        bat.restart()
        ball.restart(-65)
        scoreboard.level_up()
        scoreboard.update_scoreboard()
        create_bricks()
        play_game()


def play_game():
    touches = 0
    while scoreboard.lives > 0 and brick.brick_list != []:
        # ball continuous movement
        # set ball speed
        time.sleep(ball.move_speed)
        screen.update()
        ball.forward(10)

        # Create bounce from paddle
        # Create bounce from roof and floor
        if ball.distance(bat) < 40:
            if ball.xcor() > bat.xcor():
                ball.setheading(180 - ball.heading())
                ball.setheading(360 - ball.heading())

            else:
                ball.setheading(360 - ball.heading())

            for i in range(0,4):
                time.sleep(ball.move_speed)
                screen.update()
                ball.forward(10)



        if ball.ycor() > 300:
            ball.setheading(360 - ball.heading())
            for i in range(0,4):
                time.sleep(ball.move_speed)
                screen.update()
                ball.forward(10)


        # Create bounce from walls
        if ball.xcor() > 550 or ball.xcor() < -550:
            ball.setheading(180 - ball.heading())
            for i in range(0,4):
                time.sleep(ball.move_speed)
                screen.update()
                ball.forward(10)



        # lose state
        if ball.ycor() < -360:
            # sleep screen for smoothness with ball return
            time.sleep(1)
            screen.update()
            ball.restart(-65)
            bat.restart()
            scoreboard.lives -= 1
            scoreboard.update_scoreboard()

        # hit bricks
        # Keep score
        # speed up ball

        for hit_brick in brick.brick_list:
            index = brick.brick_list.index(hit_brick)

            if hit_brick.distance(ball) < 60:
                hit_brick.goto(1000, 1000)
                if ball.xcor() > hit_brick.xcor():
                    ball.setheading(180 - ball.heading())
                if ball.ycor() < hit_brick.ycor():
                    ball.setheading(360 - ball.heading())
                time.sleep(ball.move_speed)
                screen.update()
                ball.forward(10)

                touches +=1
                brick.remove_brick(index)

                if hit_brick.color()[0] == 'red':
                    scoreboard.update_score(7)
                    scoreboard.update_scoreboard()
                    ball.speed_up()
                if hit_brick.color()[0] == 'orange':
                    scoreboard.update_score(5)
                    scoreboard.update_scoreboard()

                if hit_brick.color()[0] == 'green':
                    scoreboard.update_score(3)
                    scoreboard.update_scoreboard()

                if hit_brick.color()[0] == 'yellow':
                    scoreboard.update_score(1)
                    scoreboard.update_scoreboard()
                    ball.speed_up()
        if touches == 4:
            ball.speed_up()
            touches = 0


    outcome()


play_game()




screen.exitonclick()
