import turtle
t = turtle.Turtle()
t.speed(0)

for i in range (180):
				t.color("black")
				t.circle(190 - i, 90)
				t.left(90)
				t.color("purple")
				t.circle(190 - i, 90)
				t.left (90)
				t.circle(190 - i, 90)
				t.left(90)
				t.color('#E5B8F4')
				t.circle(190 - i, 90)
				t.left (18)
t.done()			