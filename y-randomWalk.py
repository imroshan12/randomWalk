from turtle import Turtle, Screen
from random import choice
import randomcolor

t = Turtle()
t.pensize(6)
t.speed(7)
directions = [0, 90, 180, 270]

t.setheading(180)
t.forward(30)

i = 0
while i < 500:
    t.color(randomcolor.RandomColor().generate())
    t.setheading(choice(directions))
    t.forward(20)
    i += 1

Screen().exitonclick()
