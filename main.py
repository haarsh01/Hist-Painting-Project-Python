#import colorgram
#rgb_colors =[]
#colors = colorgram.extract('image.jpg',30)
#for color in colors:
 #  r= color.rgb.r
 #  g= color.rgb.g
  # b=color.rgb.b
 #  new_color = (r, g, b)
  # rgb_colors.append(new_color)
#print(rgb_colors)
import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
color_list = [(245, 243, 239), (246, 241, 244), (203, 165, 108), (239, 245, 240), (235, 238, 244), (154, 74, 47), (222, 201, 136), (51, 93, 124), (171, 153, 40), (138, 31, 20), (132, 162, 185), (199, 91, 71), (47, 122, 88), (14, 100, 73), (146, 178, 147), (94, 73, 75), (72, 48, 39), (234, 176, 164), (162, 143, 158), (55, 46, 50), (184, 205, 172), (19, 85, 88), (42, 62, 74), (147, 20, 23), (85, 145, 127), (183, 86, 88), (45, 66, 84), (107, 127, 152), (221, 172, 176), (14, 72, 67)]

tim.setheading(255)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)