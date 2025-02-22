from turtle import Turtle

class SnakeCreator:
    counter = 0
    def __init__(self):
        """ Initialize each segment with its position and color. """
        self.anie = Turtle("square")
        self.anie.penup()
        file = open("data.txt",mode="r")
        self.high_score = int(file.read())
        self.id = SnakeCreator.counter
        x =( -20 * self.id) if self.id<3 else -500 
        self.anie.goto(x, y = 0) 
        SnakeCreator.counter += 1
    def move(self):
        """ Move the head forward. """
        self.anie.forward(20)

    def move_forward(self):
        """ Set heading up and move forward. """
        if self.anie.heading()!=270:
            self.anie.setheading(90)

    def move_backward(self):
        """ Set heading down and move forward. """
        if self.anie.heading()!=90:
            self.anie.setheading(270)

    def move_left(self):
        """ Set heading left and move forward. """
        if self.anie.heading()!=0:
            self.anie.setheading(180)

    def move_right(self):
        """ Set heading right and move forward. """
        if self.anie.heading()!=180:
            self.anie.setheading(0)
