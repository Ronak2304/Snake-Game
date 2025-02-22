from turtle import Turtle,Screen,colormode 
import random 

colormode(255)
r = random.randint(0,255)
g = random.randint(0,255)
b = random.randint(0,255)
class Food(Turtle):
    score = 0
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_wid=0.5,stretch_len=0.5)
        self.color((r,g,b))
        self.penup()
        self.speed("fastest")
        self.goto(x=random.randint(-280,280),y=random.randint(-230,230))

