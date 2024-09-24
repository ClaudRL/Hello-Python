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

draw_shape(5, 60, "blue")
agui.clear()
draw_shape(7, 45, "red")
agui.clear()
draw_shape(3, 50, "black")
agui.clear()