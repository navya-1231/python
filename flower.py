import turtle
t=turtle.Turtle()
t.speed(10)
def flower():
    for i in range(5):
        t.fillcolor("red")
        t.begin_fill()
        t.circle(190-i,90)
        t.left(90)
        t.circle(190 - i, 90)
        t.end_fill()
        t.left(18)

        
flower()
t.hideturtle()
turtle.done()
