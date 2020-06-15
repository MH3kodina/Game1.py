# Simple pong in python 3 for beginners.
# By amin-fatehi.
# part 1 : Getting started.

import turtle

wn = turtle.Screen()
wn.title("pong by amin-fatehi")
wn.bgcolor("black")
wn.setup(width = 800 , height = 600)
wn.tracer(0)

# Main game loop
while True:
    wn.update()
