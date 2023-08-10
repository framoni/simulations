from itertools import combinations
from math import atan2, degrees, dist, sqrt
import turtle


def orient_turtle_to_point(turtle_obj, x, y):
    angle = degrees(atan2(y - turtle_obj.ycor(), x - turtle_obj.xcor()))
    turtle_obj.setheading(angle)


def same_position(turtles_obj):
    positions = [t.pos() for t in turtles_obj]
    for comb in combinations(positions, 2):
        if dist(*comb) > 1:
            return False
    return True


def init_turtle(color, x, y):
    puppy = turtle.Turtle()
    puppy.color(color)
    puppy.shape('turtle')
    puppy.pensize(5)
    puppy.penup()
    puppy.setpos(x, y)
    puppy.pendown()
    return puppy


def draw_triangle(side):
    picasso = turtle.Turtle()
    picasso.color('navy')
    picasso.shape('turtle')
    picasso.pensize(5)
    picasso.penup()
    picasso.setpos(-side/2, -side*sqrt(3)/6)
    picasso.pendown()
    picasso.forward(side)
    picasso.left(120)
    picasso.forward(side)
    picasso.left(120)
    picasso.forward(side)


def step(turtles_obj):
    for t in turtles_obj:
        t.forward(1)


def main():
    wn = turtle.Screen()
    wn.bgcolor("SeaGreen2")

    side = 400

    draw_triangle(side)

    pietro = init_turtle("hotpink", 0, side*sqrt(3)/3)
    valerio = init_turtle("orangered", -side/2, -side*sqrt(3)/6)
    rino = init_turtle("indianred", side/2, -side*sqrt(3)/6)

    turtles_obj = [pietro, rino, valerio]
    
    while not same_position(turtles_obj):
        step(turtles_obj)
        for idx, t in enumerate(turtles_obj):
            orient_turtle_to_point(t, *turtles_obj[idx-1].pos())

    wn.exitonclick()


if __name__ == '__main__':
    main()
