from turtle import Screen
from paddle import Paddle
from ball import Ball
from bricks import Bricks
from scoreboard import Scoreboard
import time


# Our screen
screen = Screen()
screen.setup(820, 800)
screen.bgcolor("black")
screen.title("turtle_breakout")
screen.tracer(0)

# Our objects
player_paddle = Paddle((0, - 300))
ball = Ball()
bricks = Bricks()
scoreboard = Scoreboard(lives=1)


pause = False
game_on = True

screen.listen()
screen.onkeypress(player_paddle.move_left, "Left")
screen.onkeyrelease(player_paddle.stop_left, "Left")
screen.onkeypress(player_paddle.move_right, "Right")
screen.onkeyrelease(player_paddle.stop_right, "Right")




while game_on:
    screen.update()
    time.sleep(0.05)
    ball.move()
    

    if ball.ycor() > 380: # Checks the roof of the game screen
        ball.bounce(x_bounce=False, y_bounce=True)

    if ball.xcor() > 370 or ball.xcor() < -370: # Checks the sides of the screen
        ball.bounce(x_bounce=True, y_bounce=False)


    if ball.ycor() < -400: # Will reset the ball once it hits the ground
        ball.ball_reset()
        scoreboard.lives -= 1
        scoreboard.update_scoreboard()

    
    if ball.distance(player_paddle) < 90 and ball.ycor() < -270:
        # If the paddle is on the right side of the screen
        if player_paddle.xcor() < 0:
            if ball.xcor() > player_paddle.xcor(): # The if statement will check if the ball hits the left side of the paddle, because we want it to go back left
                ball.bounce(x_bounce=True, y_bounce=True) # The function comes in handy here, where we can just adjust the different bounce properties
            else:
                ball.bounce(x_bounce=False, y_bounce=True) # If the paddle hits the right side of the paddle, it should just bounce it normally.

        # If the paddle is on the left of the screen
        elif player_paddle.xcor() > 0: 
            if ball.xcor() < player_paddle.xcor(): # The if statement will check if the ball hits the right side of the paddle, because we want it to go back left
                ball.bounce(x_bounce=True, y_bounce=True) # Once again it should change direction completely
            else:
                ball.bounce(x_bounce=False, y_bounce=True) # If the paddle hist the left side of the paddle, bounce as normal!

        # If the paddle is in the middle
        else:
            if ball.xcor() > player_paddle.xcor():
                ball.bounce(x_bounce=True, y_bounce=True)
            elif ball.xcor() < player_paddle.xcor():
                ball.bounce(x_bounce=True, y_bounce=True)
            else:
                ball.bounce(x_bounce=False, y_bounce=True)

    
    for brick in bricks.bricks:
        if ball.distance(brick) < 40:

            brick.clear()
            brick.goto(3000, 3000)
            bricks.bricks.remove(brick)
            scoreboard.give_points()
            scoreboard.update_scoreboard()
            

            # detect collision from left
            if ball.xcor() < brick.left_wall:
                ball.bounce(x_bounce=True, y_bounce=False)

            # detect collision from right
            elif ball.xcor() > brick.right_wall:
                ball.bounce(x_bounce=True, y_bounce=False)

            # detect collision from bottom
            elif ball.ycor() < brick.bottom_wall:
                ball.bounce(x_bounce=False, y_bounce=True)

            # detect collision from top
            elif ball.ycor() > brick.upper_wall:
                ball.bounce(x_bounce=False, y_bounce=True)
        
        if scoreboard.lives < 0:
            game_on = False
            scoreboard.update_high_scores()

        elif len(bricks.bricks) == 0:
            game_on = False
            scoreboard.update_high_scores()