import turtle
screen = turtle.Screen()
screen.bgcolor("lightblue")  
screen.title("Drawing Polygons")
t = turtle.Turtle()
t.speed(5)
t.pensize(3)
# Function to draw and fill any polygon
def draw_polygon(sides, length, fill_color):
    angle = 360 / sides
    t.color("black", fill_color)  
    t.begin_fill()
    for _ in range(sides):
        t.forward(length)
        t.left(angle)
    t.end_fill()
# Draw Equilateral Triangle
t.penup()
t.goto(-200, 0)
t.pendown()
draw_polygon(3, 100, "yellow")   
# Draw Rectangle
t.penup()
t.goto(0, 0)
t.pendown()

t.color("black", "orange")
t.begin_fill()
for _ in range(2):
    t.forward(150)
    t.left(90)
    t.forward(80)
    t.left(90)
t.end_fill()
# Draw Hexagon
t.penup()
t.goto(200, 0)
t.pendown()
draw_polygon(6, 70, "lightgreen")  # 6 sides → Hexagon

t.hideturtle()
turtle.done()
