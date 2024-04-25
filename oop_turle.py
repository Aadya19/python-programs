'''import turtle
s=turtle.Turtle()
s.shape("turtle")
s.speed(0)
turtle.bgcolor("light blue")
for i in range(10):
    s.circle(10)
    s.right(5)
    s.forward(45)
    s.backward(90)
    s.circle(100)
turtle.mainloop()'''
import turtle

def koch_snowflake(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_snowflake(t, order - 1, size / 3)
            t.left(angle)

def main():
    screen = turtle.Screen()
    screen.bgcolor("black")
    t = turtle.Turtle()
    t.color("white")
    t.penup()
    t.goto(-150, 90)
    t.pendown()

    for _ in range(3):
        koch_snowflake(t, 4, 300)
        t.right(120)

    screen.mainloop()

main()