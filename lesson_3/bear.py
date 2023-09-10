from turtle import *
t = Turtle()
t.screen.setup(800, 800)

#голова

t.color('brown')
t.begin_fill()
t.circle(70)
t.end_fill()

t.up()#щеки
t.goto(0,5)
t.down()
t.color('white')
t.begin_fill()
t.circle(25)
t.end_fill()

t.up()#нос
t.goto(0,35)
t.down()
t.begin_fill()
t.color('pink')
t.circle(5)
t.end_fill()

t.up()#рот
t.goto(0,20)
t.down()
t.color('black')
t.right(55)
t.fd(10)

t.up()#рот
t.goto(0,20)
t.down()
t.color('black')
t.right(70)
t.fd(10)

t.color('brown')#ухо
t.begin_fill()
t.up()
t.goto(40,120)
t.down()
t.circle(20)
t.end_fill()

t.color('brown')#ухо
t.begin_fill()
t.up()
t.goto(-75,120)
t.down()
t.circle(20)
t.end_fill()

t.up()#глаз
t.goto(20,70)
t.down()
t.begin_fill()
t.color('black')
t.circle(5)
t.end_fill()

t.up()#глаз
t.goto(-30,70)
t.down()
t.begin_fill()
t.color('black')
t.circle(5)
t.end_fill()

#тело

t.up()
t.goto(-90,-45)
t.down()
t.begin_fill()
t.color('brown')
t.circle(110)
t.end_fill()

#ноги
#правая нога

t.up()
t.goto(60,-180)
t.down()
t.color('brown')
t.begin_fill()
t.circle(30)
t.end_fill()
t.color('black')
t.circle(30)

t.color('pink')
t.up()
t.goto(70,-200)
t.down()
t.begin_fill()
t.circle(17)
t.end_fill()
t.color('black')
t.circle(17)

t.color('pink')
t.up()
t.goto(72,-182)
t.down()
t.begin_fill()
t.circle(3)
t.end_fill()

t.color('pink')
t.up()
t.goto(82,-180)
t.down()
t.begin_fill()
t.circle(3)
t.end_fill()

t.color('pink')
t.up()
t.goto(92,-182)
t.down()
t.begin_fill()
t.circle(3)
t.end_fill()


#левая нога
t.up()
t.goto(-110,-180)
t.down()
t.color('brown')
t.begin_fill()
t.circle(30)
t.end_fill()
t.color('black')
t.circle(30)

t.color('pink')
t.up()
t.goto(-100,-200)
t.down()
t.begin_fill()
t.circle(17)
t.end_fill()
t.color('black')
t.circle(17)

t.color('pink')
t.up()
t.goto(-90,-180)
t.down()
t.begin_fill()
t.circle(3)
t.end_fill()

t.color('pink')
t.up()
t.goto(-100,-182)
t.down()
t.begin_fill()
t.circle(3)
t.end_fill()

t.color('pink')
t.up()
t.goto(-80,-182)
t.down()
t.begin_fill()
t.circle(3)
t.end_fill()



#рука левая

t.color('brown')
t.begin_fill()
t.up()
t.goto(-100,-45)
t.down()
t.circle(30)
t.end_fill()
t.color('black')
t.circle(30)

t.up()#пальцы
t.goto(-100,-45)
t.down()
t.color('black')
t.right(270)
t.fd(15)

t.up()#пальцы
t.goto(-90,-35)
t.down()
t.color('black')
t.right(380)
t.fd(15)

t.up()
t.goto(-90,-35)
t.down()
t.setheading(20)
for i in range(4):
    t.circle(12, 180)
    t.circle(-12, 180)

t.up()
t.goto(-150,90)
t.down() 
t.color('red')
t.begin_fill()
t.circle(55)
t.end_fill()

t.setheading(100)
t.begin_fill()
t.right(120)
t.forward(15)
t.right(120)
t.forward(15)

t.end_fill()


#рука правая

t.color('brown')
t.begin_fill()
t.up()
t.goto(55,-40)
t.down()
t.circle(30)
t.end_fill()
t.color('black')
t.circle(30)

t.up()#пальцы
t.goto(45,-70)
t.down()
t.right(190)
t.color('black')
t.fd(15)

t.up()#пальцы
t.goto(50,-80)
t.down()
t.color('black')
t.fd(20)



t.ht()



t.screen.exitonclick()
t.screen.mainloop()

