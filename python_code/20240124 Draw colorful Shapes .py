# Draw Shapes

import turtle

agui = turtle.Turtle()

def draw_shape(side,length,color):
    agui.color(color)
    agui.begin_fill()
    agui.speed(2)
    for _ in range(side): # _ 被用作占位符
        agui.forward(length)
        agui.right(360/side)
    agui.end_fill()

# Input for the first Triangles
#side1 = int(input("Enter the length of the Triangles: "))
#length1 = float(input("Enter the length of the Triangles: "))
#draw_shape(side1,dlength1,color1)
draw_shape(5, 60, "blue")
turtle.clear()
draw_shape(7, 45, "red")
turtle.clear()
draw_shape(3, 50, "black")
turtle.done()