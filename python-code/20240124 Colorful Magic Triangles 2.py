# Colorful Magic Triangles 2

import turtle

agui = turtle.Turtle()

def draw_filled_Triangles(length,fill_color):
    agui.color(fill_color)
    agui.begin_fill()
    agui.speed(2)
    for _ in range(3): # _ 被用作占位符
        agui.forward(length)
        agui.left(120)
    agui.end_fill()
    return length

# Input for the first Triangles
length1 = float(input("Enter the length of the Triangles: "))
color1 = "pink"
agui.left(60)
draw_filled_Triangles(length1,color1)

agui.left(60)
color1 = "red"
draw_filled_Triangles(length1,color1)

agui.left(60)
color1 = "yellow"
draw_filled_Triangles(length1,color1)

agui.left(60)
color1 = "brown"
draw_filled_Triangles(length1,color1)

agui.left(60)
color1 = "purple"
draw_filled_Triangles(length1,color1)

agui.left(60)
color1 = "blue"
draw_filled_Triangles(length1,color1)