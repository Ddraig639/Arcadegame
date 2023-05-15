# importing libraries
import turtle
import random
import time

# creating turtle screen
screen = turtle.Screen()
screen.title('DATAFLAIR-SNAKE GAME')
screen.setup(width=700, height=700)
screen.tracer(0)
turtle.bgcolor('turquoise')

##creating a border for our game

turtle.speed(5)
turtle.pensize(4)
turtle.penup()
turtle.goto(-310, 250)
turtle.pendown()
turtle.color('black')
turtle.forward(600)
turtle.right(90)
turtle.forward(500)
turtle.right(90)
turtle.forward(600)
turtle.right(90)
turtle.forward(500)
turtle.penup()
turtle.hideturtle()

# score
score = 0
delay: float = 0.1

# snake
snake = turtle.Turtle()

snake.shape('square')
snake.pensize(10)
snake.color("black")
snake.penup()
snake.goto(250, 200)
snake.direction = 'stop'

zack=snake.clone()
zack.goto(250, -200)
zack.fillcolor("green")

snake1=snake.clone()
snake1.goto(100, 150)

zack1=zack.clone()
zack1.goto(100, -150)
snake2=snake.clone()
snake2.goto(100, 270)

zack2=zack.clone()
zack2.goto(100, -270)

snake3=snake.clone()
snake3.goto(100, 150)

zack3=zack.clone()
zack3.goto(100, -150)
bird = turtle.Turtle()
bird.speed(0)
bird.shape('turtle')
bird.color("black")
bird.penup()
bird.goto(0, 0)
bird.direction = 'stop'


# scoring
scoring = turtle.Turtle()
scoring.speed(0)
scoring.color("black")
scoring.penup()
scoring.hideturtle()
scoring.goto(0, 300)
scoring.write("Score :", align="center", font=("Courier", 24, "bold"))


#######define how to move
def snake_go_up():
    if snake.direction != "down":
        snake.direction = "up"


def snake_go_down():
    if snake.direction != "up":
        snake.direction = "down"

def snake_go_left():
    if snake.direction != "right":
        snake.direction = "left"
    if zack.direction != "right":
        zack.direction = "left"
    if snake1.direction != "right":
        snake1.direction = "left"
    if zack1.direction != "right":
        zack1.direction = "left"
    if snake2.direction != "right":
        snake2.direction = "left"
    if zack2.direction != "right":
        zack2.direction = "left"
    if snake3.direction != "right":
        snake3.direction = "left"
    if zack3.direction != "right":
        zack3.direction = "left"

    bird.direction="up"


def snake_go_right():
    if snake.direction != "left":
        snake.direction = "right"
    if zack.direction != "left":
        zack.direction = "right"




def snake_move():
    if snake.direction == "up":
        y = snake.ycor()
        snake.sety(y + 20)

    if snake.direction == "down":
        y = snake.ycor()
        snake.sety(y - 20)

    if snake.direction == "left":
        x = snake.xcor()
        snake.setx(x - 20)
    if zack.direction == "left":
        x = zack.xcor()
        zack.setx(x - 20)
    if snake1.direction == "left":
        x = snake1.xcor()
        snake1.setx(x - 20)
    if zack1.direction == "left":
        x = zack1.xcor()
        zack1.setx(x - 20)
    if snake2.direction == "left":
        x = snake2.xcor()
        snake2.setx(x - 20)
    if zack2.direction == "left":
        x = zack2.xcor()
        zack2.setx(x - 20)
    if snake3.direction == "left":
        x = snake3.xcor()
        snake3.setx(x - 20)
    if zack3.direction == "left":
        x = zack3.xcor()
        zack3.setx(x - 20)

    if bird.direction == "up":
        y = bird.ycor()
        bird.sety(y + 20)

    if bird.direction == "down":
        y = bird.ycor()
        bird.sety(y - 3)


    bird.direction="down"




# Keyboard bindings
screen.listen()
screen.onkeypress(snake_go_left)
def dead():
    screen.clear()
    scoring.goto(0, 0)
    scoring.write("    GAME OVER \n Your Score is {}".format(score), align="center",
                  font=("Courier", 30, "bold"))


# main loop

while True:
    screen.update()

        ## creating new_ball

    # adding ball to snake
    snake_move()

    ##snake and border collision
    if snake.xcor() > 280 or snake.xcor() < -300 or snake.ycor() > 240 or snake.ycor() < -240:
        x = random.randint(260, 270)
        y = random.randint(-240, 240)
        snake.goto(x, y)
        scoring.clear()
        score += 1
        scoring.write("Score:{}".format(score), align="center", font=("Courier", 24, "bold"))

    if zack.xcor() > 280 or zack.xcor() < -300 or zack.ycor() > 240 or zack.ycor() < -240:
        x = random.randint(260, 270)
        y = random.randint(-240, 240)
        zack.goto(x, y)
        scoring.clear()
        score += 1
        scoring.write("Score:{}".format(score), align="center", font=("Courier", 24, "bold"))

    if snake1.xcor() > 280 or snake1.xcor() < -300 or snake1.ycor() > 240 or snake1.ycor() < -240:
        x = random.randint(260, 270)
        y = random.randint(-240, 240)
        snake1.goto(x, y)
        scoring.clear()
        score += 1
        scoring.write("Score:{}".format(score), align="center", font=("Courier", 24, "bold"))

    if zack1.xcor() > 280 or zack1.xcor() < -300 or zack1.ycor() > 240 or zack1.ycor() < -240:
        x = random.randint(260, 270)
        y = random.randint(-240, 240)
        zack1.goto(x,y)
        scoring.clear()
        score += 1
        scoring.write("Score:{}".format(score), align="center", font=("Courier", 24, "bold"))

    if snake2.xcor() > 280 or snake2.xcor() < -300 or snake2.ycor() > 240 or snake2.ycor() < -240:
        x = random.randint(260, 270)
        y = random.randint(-240, 240)
        snake2.goto(x, y)
        scoring.clear()
        score += 1
        scoring.write("Score:{}".format(score), align="center", font=("Courier", 24, "bold"))

    if zack2.xcor() > 280 or zack2.xcor() < -300 or zack2.ycor() > 240 or zack2.ycor() < -240:
        x = random.randint(260, 270)
        y = random.randint(-240, 240)
        zack2.goto(x, y)
        scoring.clear()
        score += 1
        scoring.write("Score:{}".format(score), align="center", font=("Courier", 24, "bold"))

    if snake3.xcor() > 280 or snake3.xcor() < -300 or snake3.ycor() > 240 or snake3.ycor() < -240:
        x = random.randint(260, 270)
        y = random.randint(-240, 240)
        snake3.goto(x, y)
        scoring.clear()
        score += 1
        scoring.write("Score:{}".format(score), align="center", font=("Courier", 24, "bold"))

    if zack3.xcor() > 280 or zack3.xcor() < -300 or zack3.ycor() > 240 or zack3.ycor() < -240:
        x = random.randint(260, 270)
        y = random.randint(-240, 240)
        zack3.goto(x, y)
        scoring.clear()
        score += 1
        scoring.write("Score:{}".format(score), align="center", font=("Courier", 24, "bold"))

    ## snake collision
    if bird.distance(snake) < 20:
        dead()
        break
    if bird.distance(zack) < 20:
        dead()
        break
    if bird.distance(snake1) < 20:
        dead()
        break
    if bird.distance(zack1) < 20:
        dead()
        break
    if bird.distance(snake2) < 20:
        dead()
        break
    if bird.distance(zack2) < 20:
        dead()
        break
    if bird.distance(snake3) < 20:
        dead()
        break
    if bird.distance(zack3) < 20:
        dead()
        break

    delay -= 0.000000001
    time.sleep(delay)
turtle.Terminator()






