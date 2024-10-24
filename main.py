# import colorgram

# rgb_colours  = []
# colours = colorgram.extract('image.jpg',80)

# for colour in colours:
#     r = colour.rgb.r
#     g = colour.rgb.g
#     b = colour.rgb.b
#     rgb_colours.append((r,g,b))

# print(rgb_colours)
import turtle as t
import random

t.colormode(255)
colour_list = [(207, 158, 82), (54, 89, 130), (144, 91, 40), (139, 27, 50), (221, 207, 105), (132, 177, 202), (157, 47, 83), (45, 55, 104), (169, 160, 40), (130, 189, 143), (83, 20, 44), (38, 43, 65), (186, 93, 107), (186, 140, 171), (86, 118, 179), (58, 39, 32), (89, 156, 93), (79, 153, 164), (195, 80, 72), (79, 74, 44), (45, 74, 77), (59, 128, 120), (162, 202, 216), (44, 76, 76), (220, 175, 186), (178, 188, 213), (170, 207, 173), (151, 36, 33), (223, 178, 170), (40, 62, 61)]
tim = t.Turtle()
tim.hideturtle()
tim.speed("fastest")

tim.penup()
tim.setheading(220)
tim.forward(300)
tim.setheading(0)


for _ in range(10):
    for _ in range(10):
        tim.dot(20,random.choice(colour_list))
        tim.penup()
        tim.forward(50)

    tim.penup()
    tim.left(90)
    tim.forward(50)
    tim.left(90)
    tim.forward(100*5)
    tim.right(180)



screen = t.Screen()
screen.exitonclick()
    