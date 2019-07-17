#Welcome to ZodiacAnimation
#Github profile :- gitzodiac
#let's jump over

#python3.x
#tuttle

from turtle import *
import random
t = Turtle()

for step in range(10):
    pencolor(random.choice(["red","blue","green","yellow","violet","purple","black"]))
    pensize(random.randint(3,10))
    fd(100)
    rt(180)
    backward(20)
    lt(45)
    fd(30)
    lt(random.choice([15,25,35,45,55,65]))
    backward(20)

print(Done)
