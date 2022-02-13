import turtle
import time

# draw screen
screen = turtle.Screen()
screen.title("My Pong")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

# draw paddle 1
paddle_1 = turtle.Turtle()
paddle_1.speed(0)
paddle_1.shape("square")
paddle_1.color("white")
paddle_1.shapesize(stretch_wid=5, stretch_len=1)
paddle_1.penup()
paddle_1.goto(-350, 0)

# draw paddle 2
paddle_2 = turtle.Turtle()
paddle_2.speed(0)
paddle_2.shape("square")
paddle_2.color("white")
paddle_2.shapesize(stretch_wid=5, stretch_len=1)
paddle_2.penup()
paddle_2.goto(350, 0)

# draw ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 4
ball.dy = 4

# score
score_1 = 0
score_2 = 0

# head-up display
hud = turtle.Turtle()
hud.speed(0)
hud.shape("square")
hud.color("white")
hud.penup()
hud.hideturtle()
hud.goto(0, 260)
hud.write("Player 1: 0             :             Player 2: 0", align="center", font=("Press Start 2P", 24, "normal"))


# movement
def move_up_paddles(paddle):
    y = paddle.ycor()
    if y < 250:
        y += 30
        if (y > 250):
            y = 250
    else:
        y = 250
    paddle.sety(y)


def move_down_paddles(paddle):
    y = paddle.ycor()
    if y > -250:
        y += -30
        if (y < -250):
            y = -250
    else:
        y = -250
    paddle.sety(y)


def paddle_1_up():
    move_up_paddles(paddle_1)


def paddle_1_down():
    move_down_paddles(paddle_1)


def paddle_2_up():
    move_up_paddles(paddle_2)


def paddle_2_down():
    move_down_paddles(paddle_2)

# keyboard
screen.listen()
screen.onkeypress(paddle_1_up, "w")
screen.onkeypress(paddle_1_down, "s")
screen.onkeypress(paddle_2_up, "Up")
screen.onkeypress(paddle_2_down, "Down")



while True:
    fps = 1 / 60
    time.sleep(fps)
    screen.update()
    screen.update()

    # ball movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # collision with the upper wall
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    # collision with lower wall
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    # collision with left wall
    if ball.xcor() < -390:
        score_2 += 1
        hud.clear()
        hud.write(
            "Player 1: {}             :             Player 2: {}"
            .format(score_1, score_2),
            align="center",
            font=("Press Start 2P", 24, "normal"),
        )
        ball.goto(0, 0)
        ball.dx *= -1

    # collision with right wall
    if ball.xcor() > 390:
        score_1 += 1
        hud.clear()
        hud.write(
            "Player 1: {}             :             Player 2: {}"
            .format(score_1, score_2),
            align="center",
            font=("Press Start 2P", 24, "normal"),
        )
        ball.goto(0, 0)
        ball.dy *= 1
        ball.dx *= -1

    size_paddle_1 = 55
    size_paddle_2 = 55

    # collision with the paddle 1
    if (ball.xcor() < -330 and not (ball.xcor() < -340)) and paddle_1.ycor()\
            + size_paddle_1 > ball.ycor() > paddle_1.ycor() - size_paddle_1:
        ball.goto(-330, ball.ycor())
        ball.dx *= -1
    
    elif paddle_1.ycor() + size_paddle_1 > ball.ycor() > paddle_1.ycor() - size_paddle_1 and ball.xcor() < -330:
        ball.dx *= -1.1
        ball.dy *= -1
        if ball.xcor() < -345:
            ball.dx *= -1

    # collision with the paddle 2
    if (ball.xcor() > 330 and not (ball.xcor() > 340)) and paddle_2.ycor()\
            + size_paddle_2 > ball.ycor() > paddle_2.ycor() - size_paddle_2:
        ball.goto(330, ball.ycor())
        ball.dx *= -1.1

    elif paddle_2.ycor() + size_paddle_2 > ball.ycor() > \
            paddle_2.ycor() - size_paddle_2 and ball.xcor() > 330:
        ball.dx *= -1
        ball.dy *= -1
        if ball.xcor() > 345:
            ball.dx *= -1.1

  


    