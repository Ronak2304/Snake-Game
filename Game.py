from turtle import Screen,Turtle
import time
from snake import SnakeCreator
from food import Food
import random


my_screen = Screen()
my_screen.setup(600, 500)
my_screen.bgpic("finalbgGif.gif")
my_screen.tracer(0)

""" Creating snake objects """
snake = []
for i in range(3):
    obj = SnakeCreator()  # Pass index to set initial position
    snake.append(obj)

khana = Food()
score = Turtle()
score.shapesize(stretch_len=10,stretch_wid=10)
score.penup()
score.color("white")
score.hideturtle()
score.goto(x=0,y=200)
score.write(f"Score: {khana.score}",font=("Arial",15,"bold"),align="center")


high_score = Turtle()
prev_high_score = 0
high_score.shapesize(stretch_len=10,stretch_wid=10)
high_score.penup()
high_score.color("white")
high_score.hideturtle()
high_score.goto(x=-200,y=200)
high_score.write(f"High Score: {snake[0].high_score}",font=("Arial",15,"bold"),align="center")
game_is_on = True

# Key bindings
my_screen.listen()
my_screen.onkeypress(fun= snake[0].move_forward, key="Up")
my_screen.onkeypress(fun= snake[0].move_backward, key="Down")
my_screen.onkeypress(fun= snake[0].move_left, key="Left")
my_screen.onkeypress(fun= snake[0].move_right, key="Right")

while game_is_on:
    """ Refreshes the screen after every 0.1 sec """
    my_screen.update()
    time.sleep(0.1)
    for i in range(len(snake) - 1, 0, -1):
        new_x = snake[i - 1].anie.xcor()
        new_y = snake[i - 1].anie.ycor()
        snake[i].anie.goto(new_x, new_y)
    snake[0].move()  # Move the head forward continuously
    # if (snake[0].anie.xcor() == khana.xcor()) and (snake[0].anie.ycor() == (khana.ycor()*2.5)):
    if snake[0].anie.distance(khana)<15:
        score.clear()
        khana.score+=1
        score.write(f"Score: {khana.score}",align="center",font=("Arial",15,"bold"))
        khana.hideturtle()
        khana.goto(x=random.randint(-280,280),y=random.randint(-230,230))
        khana.showturtle()
        new_obj = SnakeCreator()
        new_obj.anie.hideturtle()
        snake.append(new_obj)
        new_obj.anie.showturtle()

    if ((snake[0].anie.xcor()>=296) or (snake[0].anie.xcor()<= -296) or (snake[0].anie.ycor()>=246) or (snake[0].anie.ycor()<=-246)):
        score.clear()
        for i in range(len(snake)-1,2,-1):
            snake[i].anie.goto(1000,1000)
            del(snake[i])
            
        data = (snake[0].high_score)
        if khana.score>data:
            with open("data.txt", "w") as w:
                w.write(str(khana.score))
            data = khana.score
            high_score.clear()
            high_score.write(f"Hgh Score: {data}",font=("Arial",15,"bold"),align="center")
        khana.score = 0
        score.write(f"Score: {khana.score}",font=("Arial",15,"bold"),align="center")
        snake[0].anie.goto(x=0,y=0)
        

    for i in range(len(snake)-1,2,-1): 
        print(i)
        if (snake[0].anie.distance(snake[i].anie))<20:
            score.clear()
            for i in range(len(snake)-1,2,-1):
                snake[i].anie.goto(1000,1000)
                del(snake[i])
            data = snake[0].high_score
            if khana.score>data:
                with open("data.txt", "w") as w:
                    w.write(str(khana.score))
                data = khana.score
                high_score.clear()
                high_score.write(f"High Score: {data}",font=("Arial",15,"bold"),align="center")
            khana.score = 0
            score.write(f"Score: {khana.score}",font=("Arial",15,"bold"),align="center")
            snake[0].anie.goto(x=0,y=0)



my_screen.exitonclick()
