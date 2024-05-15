import turtle as t


def draw_star(points,size,col,x,y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    angle=180 - (180 / points)
    t.color('red')
    t.begin_fill()
    for i in range(points):
        t.forward(size)
        t.right(angle)
        t.penup()
    t.goto(x, y)
    t.pendown()
    angle = 180 - (180 / points)
    t.color(col)
    t.begin_fill()
    for i in range(points):
        t.forward(size)
        t.right(angle)
t.end_fill()
t.Screen().bgcolor('dark blue')
draw_star(5, 50, 'yellow', 0, 0)
input()