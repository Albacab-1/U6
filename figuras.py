import turtle

turtle.speed(3)  
turtle.pensize(2) 
turtle.color("red") 

ang = 60
long = 100

turtle.penup()
turtle.goto(-200,0)
turtle.pendown()

for i in range(3):
    turtle.left(120)
    turtle.forward(50)


turtle.penup()
turtle.goto(-50,0)
turtle.pendown()
turtle.color("blue") 

for j in range(4):
    turtle.left(90)
    turtle.forward(75)


turtle.penup()
turtle.goto(140,0)
turtle.pendown()
turtle.color("yellow")

for f in range(6):
    turtle.left(60)
    turtle.forward(100)
    
turtle.done()