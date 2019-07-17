#Welcome to ZodiacAnimation
#Github profile :- gitzodiac
#let's jump over
#keep supporting


#python3.x
#tuttle

from turtle import *
import random
t = Turtle()
#t.height(1600)
t.width(1600)

for step in range(100):
    pensize(random.choice([2,3,5]))
    pencolor(random.choice(["red","black","green","blue","violet","orange"]))
    fd(random.choice([10,20,30,40,50,60,70,80,90,100]))
    rt(random.choice([45,90,30,60,180]))
    backward(25)
