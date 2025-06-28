import turtle

turtle.speed(5)  
turtle.pensize(2) 
turtle.color("red") 

ang = 60
long = 100

turtle.goto(0,0)
for i in range(6):
    turtle.right(60)
    turtle.forward(100)

    if (i==6):
        turtle.done()
