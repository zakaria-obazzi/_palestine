import turtle
h = turtle.Turtle()
h.speed(700)
oa = 7
for i in range (100):
	h.pensize(1)
	h.color("green")
	if i % 2 == 0 :
		h.pensize(oa)
		h.color("red")
	po = (i*0.7)
	h.fd(po)
	h.color("green")
	h.fd(240-po)
	if (i % 2) == 0 :
		h.lt(90)
		h.fd(0.4)
		h.lt(90)
	if (i % 2) != 0 :
		h.rt(90)
		h.fd(0.4)
		h.rt(90)		
for i in range (100,150):
	h.pensize(1)
	h.color("white")
	if i % 2 == 0 :
		h.color("red")
		h.pensize(oa)
	po = (i*0.7)
	h.fd(po)
	h.color("white")
	h.fd(240-po)
	if (i % 2) == 0 :
		h.lt(90)
		h.fd(0.4)
		h.lt(90)
	if (i % 2) != 0 :
		h.rt(90)
		h.fd(0.4)
		h.rt(90)							
for i in range (50):
	h.pensize(1)
	h.color("white")
	if i % 2 == 0 :
		h.color("red")
		h.pensize(oa)
	po = (105-(0.7*i))
	h.fd(po)
	h.color("white")
	h.fd(240-po)
	if (i % 2) == 0 :
		h.lt(90)
		h.fd(0.4)
		h.lt(90)
	if (i % 2) != 0 :
		h.rt(90)
		h.fd(0.4)
		h.rt(90)							
for i in range (50,145):
	h.pensize(1)
	h.color("black")
	if i % 2 == 0 :
		h.color("red")
		h.pensize(oa)
	po = (105-(0.7*i))
	h.fd(po)
	h.color("black")
	h.fd(240-po)
	if (i % 2) == 0 :
		h.lt(90)
		h.fd(0.4)
		h.lt(90)
	if (i % 2) != 0 :
		h.rt(90)
		h.fd(0.4)
		h.rt(90)
h.hideturtle()
turtle.done()