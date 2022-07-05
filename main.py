import random

import colorgram
from turtle import Turtle, Screen

# colors = colorgram.extract('image.jpg', 54)
# rgb = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_color = (r, g, b)
#     rgb.append(rgb_color)
#
# print(rgb)
my_turtle = Turtle()
screen = Screen()
screen.colormode(255)
# screen.screensize(500, 500)
color_list = [(240,  242, 246), (237, 231, 214), (218, 234, 224), (141, 176, 206), (25, 32, 48), (28, 105, 156),
     (208, 161, 112), (238, 222, 234), (230, 211, 94), (131, 31, 64), (5, 162, 195), (182, 45, 84), (217, 60, 85),
     (226, 80, 44), (195, 129, 168), (54, 167, 116), (29, 61, 115), (108, 181, 91), (109, 99, 88), (2, 102, 119),
     (193, 187, 47), (241, 204, 1), (19, 22, 21), (52, 149, 109), (171, 211, 173), (226, 170, 186), (150, 207, 222),
     (234, 169, 160), (184, 186, 210), (115, 38, 37), (82, 34, 76), (122, 118, 154), (28, 28, 28)]

my_turtle.hideturtle()
my_turtle.up()
my_turtle.goto(-250, -250)
my_turtle.down()
y = -250

for location in range(10):
    my_turtle.up()
    my_turtle.goto(-250, y)
    y += 50
    my_turtle.down()
    for i in range(10):
        my_turtle.dot(30, random.choice(color_list))
        my_turtle.up()
        my_turtle.fd(50)
        my_turtle.down()



screen.exitonclick()