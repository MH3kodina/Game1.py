# Simple pong in python 3 for beginners.
# By amin-fatehi.
# part 1 : Getting started.

import turtle

wn = turtle.Screen()
wn.title("pong by amin-fatehi")
wn.bgcolor("black")
wn.setup(width = 800 , height = 600)
wn.tracer(0)

# paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("red")
paddle_a.shapesize(stretch_wid=3 , stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350 , 0)
# paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("blue")
paddle_b.shapesize(stretch_wid=3 , stretch_len=1)
paddle_b.penup()
paddle_b.goto(350 ,0 )
# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("green")
ball.penup()
ball.goto(0 ,0 )
# Main game loop
while True:
    wn.update()
