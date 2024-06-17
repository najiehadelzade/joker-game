# Creating a window screen
import turtle
import math
import time

from level_2 import app

wn = turtle.Screen()
wn.addshape("media/najieh_sm.gif")
wn.addshape("media/mahbod_sm.gif")
wn.addshape("media/joker.gif")

wn.title("Snake Game")
wn.bgcolor("#42855B")
wn.setup(width=1200, height=800)

mahbod = turtle.Turtle()
mahbod.shape("media/mahbod_sm.gif")

najieh = turtle.Turtle()
najieh.shape("media/najieh_sm.gif")

fmahbod1 = turtle.Turtle()
fmahbod1.shape("media/joker.gif")
fmahbod2 = turtle.Turtle()
fmahbod2.shape("media/joker.gif")
fmahbod3 = turtle.Turtle()
fmahbod3.shape("media/joker.gif")
fmahbod4 = turtle.Turtle()
fmahbod4.shape("media/joker.gif")
fmahbod5 = turtle.Turtle()
fmahbod5.shape("media/joker.gif")
fmahbod6 = turtle.Turtle()
fmahbod6.shape("media/joker.gif")
fmahbod7 = turtle.Turtle()
fmahbod7.shape("media/joker.gif")
fmahbod8 = turtle.Turtle()
fmahbod8.shape("media/joker.gif")

najieh.penup()
mahbod.penup()
fmahbod1.penup()
fmahbod2.penup()
fmahbod3.penup()
fmahbod4.penup()
fmahbod5.penup()
fmahbod6.penup()
fmahbod7.penup()
fmahbod8.penup()

fmahbod8.setpos(0, 0)
fmahbod7.setpos(0, 0)
fmahbod6.setpos(0, 0)
fmahbod5.setpos(0, 0)
fmahbod4.setpos(200, 300)
fmahbod3.setpos(-200, -300)
fmahbod2.setpos(-300, 200)
fmahbod1.setpos(300, -200)
najieh.setpos(-500, 300)
mahbod.setpos(500, -300)

fmahbod4.left(90)
fmahbod3.left(-90)
fmahbod1.left(180)
fmahbod2.left(0)
fmahbod5.left(90)
fmahbod6.left(-90)
fmahbod7.left(180)
fmahbod8.left(0)

#taref safheh

def taeen_harkat(n, h):
    q = h.heading()
    if q == 90:
        r1 = h.ycor() + n
        return (h.xcor(), r1)
    elif q == 270:
        r2 = h.ycor() - n
        return (h.xcor(), r2)
    elif q == 0:
        t1 = h.xcor() + n
        return (t1, h.ycor())
    elif q == 180:
        t2 = h.xcor() - n
        return (t2, h.ycor())


def taeen_harkat1(n, h):
    j = taeen_harkat(n, h)
    if -550 < j[0] < 550 and -350 < j[1] < 350:
        return True

    else:
        return False

#bardashtan pen , dobareh

def pen():
    if najieh.isdown() == True:
        najieh.penup()
    else:
        najieh.pendown()


wn.onkeypress(pen, "x")


def harkat1(m):
    if m.xcor() > 500:
        m.left(180)
    elif m.xcor() < -500:
        m.left(180)
    m.forward(10)


def harkat2(n):
    if n.ycor() > 300:
        n.left(180)
    elif n.ycor() < -300:
        n.left(180)
    n.forward(10)


def faseleh(p1, p2):
    fasel = math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)
    return fasel


def harkat():
    if taeen_harkat1(10, najieh) == True:
        najieh.forward(10)

def be_chap():
    najieh.setheading(180)
    harkat()

def be_rast():
    najieh.setheading(0)
    harkat()

def be_bala():
    najieh.setheading(90)
    harkat()

def be_paein():
    najieh.setheading(270)
    harkat()

wn.onkeypress(be_rast, "d")
wn.onkeypress(be_bala, "w")
wn.onkeypress(be_chap, "a")
wn.onkeypress(be_paein, "s")


def collide(a, b):
    if faseleh(a.pos(), b.pos()) < 55:
        return True
    else:
        return False


def winmsg():
    pen = turtle.Turtle()
    pen.speed(0)
    pen.shape("square")
    pen.color("#820202")
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 250)
    pen.write("Mahbod is captured!", align="center", font=("candara", 24, "bold"))


wn.listen()
wn.tracer(0)

while True:
    wn.update()
    time.sleep(0.02)

    if (
            collide(najieh, fmahbod1) == True or
            collide(najieh, fmahbod2) == True or
            collide(najieh, fmahbod3) == True or
            collide(najieh, fmahbod4) == True or
            collide(najieh, fmahbod5) == True or
            collide(najieh, fmahbod6) == True or
            collide(najieh, fmahbod7) == True or
            collide(najieh, fmahbod8) == True
    ):
        najieh.setpos(-500, 300)
    harkat1(fmahbod1)
    harkat1(fmahbod2)
    harkat2(fmahbod5)
    harkat2(fmahbod6)
    harkat2(fmahbod3)
    harkat2(fmahbod4)
    harkat1(fmahbod7)
    harkat1(fmahbod8)
    x = collide(najieh, mahbod)
    if x == True:
        wn.bgcolor("#FFBD33")
        winmsg()
        wn.onscreenclick(lambda _, __: app())
        break

wn.mainloop()