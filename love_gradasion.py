import math
import turtle

def ky(e):
    return 16 * math.sin(e) ** 3

def jy(e):
    return 13 * math.cos(e) - 5 * \
           math.cos(2 * e) - 2 * \
           math.cos(3 * e) - \
           math.cos(4 * e)

def get_color(step, max_steps):
    # Calculate color components in range 0 to 1
    r = 1.0 - step / max_steps
    g = 0.5
    b = 1.0
    return (r, g, b)

t = turtle.Turtle()
t.speed(300)
turtle.bgcolor("black")

max_steps = 2000
for w in range(max_steps):
    color = get_color(w, max_steps)
    t.pencolor(color)

    t.goto((ky(w) * 10, jy(w) * 10))
    t.goto(0, 0)

turtle.done()
