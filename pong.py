import turtle

wn = turtle.Screen()
wn.title('Pong by TC')
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

score_a = 0
score_b = 0
ball_color = 0
colors = ["white", "green", "blue", "red", "yellow", "pink", "orange"]

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape('square')
paddle_a.color('white')
paddle_a.shapesize(stretch_wid=3, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)


# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape('square')
paddle_b.color('white')
paddle_b.shapesize(stretch_wid=3, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)


# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color(colors[ball_color])
ball.penup()
ball.goto(0, 0)
ball.dx = 0.25
ball.dy = 0.25

# Score
a = turtle.Turtle()
a.speed(0)
a.color('white')
a.penup()
a.hideturtle()
a.goto(0, 260)
a.write("Player A: {a}  Player B: {b}".format(a=score_a, b=score_b), align="center",
        font=("Courier", 24, "normal"))

# Functions


def update_score():
    return a.write("Player A: {a}  Player B: {b}".format(a=score_a, b=score_b), align="center",
                   font=("Courier", 24, "normal"))


def paddle_up(paddle):
    y = paddle.ycor()
    y += 20
    if y > 275:
        return
    else:
        paddle.sety(y)


def paddle_down(paddle):
    y = paddle.ycor()
    y -= 20
    if y < -275:
        return
    else:
        paddle.sety(y)


def tab():
    global ball_color
    if ball_color == len(colors) - 1:
        ball_color = 0
    else:
        ball_color += 1


# Keyboard binding
wn.listen()
wn.onkeypress(lambda: paddle_up(paddle_a), "w")
wn.onkeypress(lambda: paddle_down(paddle_a), "s")
wn.onkeypress(lambda: paddle_up(paddle_b), "Up")
wn.onkeypress(lambda: paddle_down(paddle_b), "Down")
wn.onkeypress(tab, "Tab")


# main game loop
while True:
    wn.update()

    ball.color(colors[ball_color])
    # Move
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border Check
    if ball.xcor() == 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        a.clear()
        update_score()

    if ball.xcor() == -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        a.clear()
        update_score()

    if ball.ycor() == 280 or ball.ycor() == -280:
        ball.dy *= -1

    # Paddle hit check
    if ball.xcor() == (paddle_a.xcor() + 10) and ball.ycor() < (paddle_a.ycor() + 30) and ball.ycor() > (paddle_a.ycor() - 30):
        ball.dx *= -1
        tab()

    if ball.xcor() == (paddle_b.xcor() - 10) and ball.ycor() < (paddle_b.ycor() + 30) and ball.ycor() > (paddle_b.ycor() - 30):
        ball.dx *= -1
        tab()
