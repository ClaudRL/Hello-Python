# Drawing 3 colorful square

import turtle

agui = turtle.Turtle()

def draw_filled_square(length, fill_color):
    agui.color(fill_color)
    agui.begin_fill()
    agui.speed(2)
    for _ in range(4):
        agui.forward(length)
        agui.left(90)
    agui.end_fill()
    return length

# Input for the first square
length1 = float(input("Enter the length of the first square: "))
color1 = input("Enter the color of the first square: ")
draw_filled_square(length1, color1)
agui.forward(length1)

# Input for the second square
length2 = float(input("Enter the length of the second square: "))
color2 = input("Enter the color of the second square: ")
draw_filled_square(length2, color2)
agui.forward(length2)

# Input for the third square
length3 = float(input("Enter the length of the third square: "))
color3 = input("Enter the color of the third square: ")
draw_filled_square(length3, color3)

turtle.done()
