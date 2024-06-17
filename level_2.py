# Creating a window screen
import turtle
import math
import time

h = 0

def app():
    wn = turtle.Screen()
    wn.clearscreen()
    wn.addshape("media/erfan_sm.gif")
    wn.addshape("media/mahbod_sm.gif")
    wn.addshape("media/najieh_sm.gif")
    wn.addshape("media/joker.gif")


    wn.title("Snake Game")
    wn.bgcolor("#42855B")
    wn.setup(width=1200, height=800)

    mahbod = turtle.Turtle()
    mahbod.shape("media/mahbod_sm.gif")
    najieh = turtle.Turtle()
    najieh.shape("media/najieh_sm.gif")
    erfan = turtle.Turtle()
    erfan.shape("media/erfan_sm.gif")
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

    fmahbod1.penup()
    fmahbod2.penup()
    fmahbod3.penup()
    fmahbod4.penup()
    fmahbod5.penup()
    fmahbod6.penup()
    fmahbod7.penup()
    fmahbod8.penup()
    najieh.penup()
    mahbod.penup()
    erfan.penup()

    fmahbod8.setpos(0, 0)
    fmahbod7.setpos(0, 0)
    fmahbod6.setpos(0, 0)
    fmahbod5.setpos(0, 0)
    fmahbod4.setpos(200, 300)
    fmahbod3.setpos(-200, -300)
    fmahbod2.setpos(-300, 200)
    fmahbod1.setpos(300, -200)
    erfan.setpos(-500, 50)
    najieh.setpos(-200, 300)
    mahbod.setpos(500, -300)

    fmahbod4.left(90)
    fmahbod3.left(-90)
    fmahbod1.left(180)
    fmahbod2.left(0)
    fmahbod5.left(90)
    fmahbod6.left(-90)
    fmahbod7.left(180)
    fmahbod8.left(0)

    def harkatx(m):
        if m.xcor() > 500:
            m.left(180)
        elif m.xcor() < -500:
            m.left(180)
        m.forward(10)

    def harkaty(n):
        if n.ycor() > 300:
            n.left(180)
        elif n.ycor() < -300:
            n.left(180)
        n.forward(10)


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



    def harkat1():
        global h
        y = collide(erfan, mahbod)
        if y == True:
            h = 1
        if h == 1:
            if taeen_harkat1(10, mahbod) == True:
                mahbod.forward(10)

        else:
            if taeen_harkat1(10, erfan) == True:
                erfan.forward(10)


    def be_chap1():
        global h
        y = collide(erfan, mahbod)
        if y == True:
            h = 1
        if h == 1:
            mahbod.setheading(180)
        else:
            erfan.setheading(180)
        harkat1()

    def be_rast1():
        global h
        y = collide(erfan, mahbod)
        if y == True:
            h = 1
        if h == 1:
            mahbod.setheading(0)
        else:
            erfan.setheading(0)
        harkat1()

    def be_bala1():
        global h
        y = collide(erfan, mahbod)
        if y == True:
            h = 1
        if h == 1:
            mahbod.setheading(90)
        else:
            erfan.setheading(90)
        harkat1()


    def be_paein1():
        global h
        y = collide(erfan, mahbod)
        if y == True:
            h = 1
        if h == 1:
            mahbod.setheading(270)
        else:
            erfan.setheading(270)
        harkat1()



    def faseleh(p1, p2):
        fasel = math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)
        return fasel


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
        pen.write("Mahbod is murdered!\nNajieh won!", align="center", font=("candara", 24, "bold"))


    wn.onkeypress(be_rast1, "k")
    wn.onkeypress(be_bala1, "u")
    wn.onkeypress(be_chap1, "h")
    wn.onkeypress(be_paein1, "j")

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

            najieh.setpos(-200, 300)
        if (
                collide(erfan, fmahbod2) == True or
                collide(erfan, fmahbod3) == True or
                collide(erfan, fmahbod1) == True or
                collide(erfan, fmahbod4) == True or
                collide(erfan, fmahbod5) == True or
                collide(erfan, fmahbod6) == True or
                collide(erfan, fmahbod7) == True or
                collide(erfan, fmahbod8) == True
        ):
            erfan.setpos(-500, 50)

        harkatx(fmahbod1)
        harkatx(fmahbod2)
        harkaty(fmahbod5)
        harkaty(fmahbod6)
        harkaty(fmahbod3)
        harkaty(fmahbod4)
        harkatx(fmahbod7)
        harkatx(fmahbod8)

        x = collide(najieh, mahbod)
        if x == True:
            wn.bgcolor("#FF5733")
            winmsg()
            break

    wn.mainloop()
