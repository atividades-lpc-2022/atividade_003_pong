from random import choice
import turtle
import time
import pygame
import winsound

VELOCITY = 1.1


def choose_starting_direction():
    return choice([1, -1])


# movement
def move_up_paddles(paddle: turtle.Turtle):
    y = paddle.ycor()
    if y < 250:
        y += 30
        if y > 250:
            y = 250
    else:
        y = 250
    paddle.sety(y)


def move_down_paddles(paddle: turtle.Turtle):
    y = paddle.ycor()
    if y > -250:
        y += -30
        if y < -250:
            y = -250
    else:
        y = -250
    paddle.sety(y)


def setup_paddle(x: int, y: int) -> turtle.Turtle:
    paddle = turtle.Turtle()
    paddle.speed(0)
    paddle.shape("square")
    paddle.color("white")
    paddle.shapesize(stretch_wid=5, stretch_len=1)
    paddle.penup()
    paddle.goto(x, y)
    return paddle


def setup_ball() -> turtle.Turtle:
    ball = turtle.Turtle()
    ball.speed(0)
    ball.shape("circle")
    ball.color("white")
    ball.penup()
    ball.goto(0, 0)
    ball.dx = 4 * choose_starting_direction()
    ball.dy = 4
    return ball


def setup_hud() -> turtle.Turtle:
    hud = turtle.Turtle()
    hud.speed(0)
    hud.shape("square")
    hud.color("white")
    hud.penup()
    hud.hideturtle()
    hud.goto(0, 260)
    hud.write(
        "Player 1: 0             :             Player 2: 0",
        align="center",
        font=("Small Fonts", 24, "normal"),
    )
    return hud


def main():
    # draw screen
    screen = turtle.Screen()
    screen.title("My Pong")
    screen.bgcolor("black")
    screen.setup(width=800, height=600)
    screen.tracer(0)

    # draw paddle 1
    paddle_1 = setup_paddle(-350, 0)

    # draw paddle 2
    paddle_2 = setup_paddle(350, 0)

    # draw ball
    ball = setup_ball()

    # score
    score_1 = 0
    score_2 = 0

    # head-up display
    hud = setup_hud()

    # keyboard
    screen.listen()
    screen.onkeypress(lambda: move_up_paddles(paddle_1), "w")
    screen.onkeypress(lambda: move_down_paddles(paddle_1), "s")
    screen.onkeypress(lambda: move_up_paddles(paddle_2), "Up")
    screen.onkeypress(lambda: move_down_paddles(paddle_2), "Down")

    for tic in range(3, 0, -1):
        hud.clear()
        hud.write(
            f"Jogo inicia em {tic}",
            align="center",
            font=("Small Fonts", 24, "normal"),
        )
        ball.dx = 0
        ball.dy = 0
        time.sleep(1)

    ball.dx = 4 * choose_starting_direction()
    ball.dy = 4

    hud.clear()
    hud.write(
        "Player 1: {}             :             Player 2: {}".format(score_1, score_2),
        align="center",
        font=("Small Fonts", 24, "normal"),
    )

    # sound effects
    pygame.mixer.init()
    py_sound = pygame.mixer.music

    while True:
        fps = 1 / 60
        time.sleep(fps)
        screen.update()

        # ball movement
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        # collision with the upper wall
        if ball.ycor() > 290:
            ball.sety(290)
            ball.dy *= -1
            winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

        # collision with lower wall
        if ball.ycor() < -290:
            ball.sety(-290)
            ball.dy *= -1
            winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

        # collision with left wall
        if ball.xcor() < -390:
            score_2 += 1
            hud.clear()
            hud.write(
                "Player 1: {}             :             Player 2: {}".format(
                    score_1, score_2
                ),
                align="center",
                font=("Small Fonts", 24, "normal"),
            )
            ball.goto(0, 0)
            ball.dx *= -1
            winsound.PlaySound("scoring.wav", winsound.SND_ASYNC)

        # collision with right wall
        if ball.xcor() > 390:
            score_1 += 1
            hud.clear()
            hud.write(
                "Player 1: {}             :             Player 2: {}".format(
                    score_1, score_2
                ),
                align="center",
                font=("Small Fonts", 24, "normal"),
            )
            ball.goto(0, 0)
            ball.dy *= 1
            ball.dx *= -1
            winsound.PlaySound("scoring.wav", winsound.SND_ASYNC)

        size_paddle_1 = 55
        size_paddle_2 = 55

        # collision with the paddle 1
        if (
            ball.xcor() < -330 and not (ball.xcor() < -340)
        ) and paddle_1.ycor() + size_paddle_1 > ball.ycor() > paddle_1.ycor() - size_paddle_1:
            winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
            ball.goto(-330, ball.ycor())
            ball.dx *= -1
        elif (
            paddle_1.ycor() + size_paddle_1
            > ball.ycor()
            > paddle_1.ycor() - size_paddle_1
            and ball.xcor() < -330
        ):
            winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
            ball.dx *= -VELOCITY
            ball.dy *= -1
            if ball.xcor() < -345:
                ball.dx *= -1

        # collision with the paddle 2
        if (
            ball.xcor() > 330 and not (ball.xcor() > 340)
        ) and paddle_2.ycor() + size_paddle_2 > ball.ycor() > paddle_2.ycor() - size_paddle_2:
            py_sound.load("bounce.wav")
            py_sound.play()
            pygame.time.wait(50)
            py_sound.stop()
            ball.goto(330, ball.ycor())
            ball.dx *= -VELOCITY
        elif (
            paddle_2.ycor() + size_paddle_2
            > ball.ycor()
            > paddle_2.ycor() - size_paddle_2
            and ball.xcor() > 330
        ):
            ball.dx *= -1
            ball.dy *= -1
            if ball.xcor() > 345:
                ball.dx *= -1.1
            py_sound.load("bounce.wav")
            py_sound.play()
            pygame.time.wait(50)
            py_sound.stop()


main()
