# import colorgram
import turtle
import random

# colors = colorgram.extract("image.jpg",30)
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
# print(rgb_colors)

zack = turtle.Turtle()
screen = turtle.Screen()
turtle.colormode(255)
color_list = [(238, 250, 244), (187, 18, 44), (243, 231, 66), (252, 235, 239), (210, 236, 242), (196, 75, 32), (218, 66, 107), (17, 124, 173), (196, 175, 17), (108, 181, 209), (12, 142, 88), (12, 166, 214), (210, 152, 96), (187, 41, 61), (241, 231, 2), (23, 39, 76), (77, 174, 94), (36, 44, 112), (215, 69, 50), (218, 130, 155), (124, 185, 119), (235, 165, 183), (5, 58, 39), (146, 209, 220), (8, 95, 55), (4, 86, 111), (162, 29, 27), (234, 171, 164), (162, 212, 176)]
zack.penup()
zack.speed(0)
zack.hideturtle()
zack.setheading(225)
zack.forward(300)
zack.setheading(0)
number_of_dot = 100

for dot_count in range(1, number_of_dot + 1):
    random_color = random.choice(color_list)
    zack.dot(20,random_color)
    zack.forward(50)

    if dot_count % 10 == 0:
        zack.setheading(90)
        zack.forward(50)
        zack.setheading(180)
        zack.forward(500)
        zack.setheading(360)



screen.exitonclick()
