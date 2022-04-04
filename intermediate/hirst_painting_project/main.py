#import colorgram
#
#colors = colorgram.extract('hirst_image.jpg',30)
#rgb_color = []
#for color in colors:
#    r = color.rgb.r
#    g = color.rgb.g
#    b = color.rgb.b
#    new_color = (r, g, b)
#    rgb_color.append(new_color)
#
#print(rgb_color)
import turtle as t
import random
screen = t.Screen()
screen.colormode(255)
t.speed("fastest")
t.hideturtle()

color_list = [(239, 236, 238), (238, 237, 236), (237, 237, 241), (26, 108, 164), (193, 38, 81), (237, 161, 50), (234, 215, 86), (227, 237, 229), (223, 137, 176), (143, 108, 57), (103, 197, 219), (21, 57, 132), (205, 166, 30), (213, 74, 91), (238, 89, 49), (142, 208, 227), (119, 191, 139), (5, 185, 177), (106, 108, 198), (137, 29, 72), (4, 162, 86), (98, 51, 36), (24, 155, 210), (229, 168, 185), (173, 185, 221), (29, 90, 95), (233, 173, 162), (156, 212, 190), (87, 46, 33), (37, 45, 83)]
for i in range(1,11):
    for j in range(1,11):
        t.pendown()
        t.dot(20, random.choice(color_list))
        t.penup()
        t.forward(50)
    t.goto(0,50 * i)


screen.exitonclick()