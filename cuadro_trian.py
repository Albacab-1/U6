import turtle 


turtle.speed(6) #establece la velocidad del puntero  (lápiz)

#secuencia del cuadrado
turtle.goto(0,0)
turtle.backward(100) 
turtle.right(90) 
turtle.backward(100) 
turtle.left(90) 
turtle.forward(100) 
turtle.right(90) 
turtle.forward(100) 

#secuencia de las líneas en diagonal
turtle.right(135) 
turtle.forward(142.423562) 
turtle.right(135) 
turtle.forward(100)
turtle.right(135) 
turtle.forward(142.423562) 
turtle.left(45)
turtle.backward(100)

turtle.speed(2)

#triangulo
turtle.left(120)
turtle.forward(59)
turtle.right(60)
turtle.forward(59)
turtle.penup()
turtle.goto(0,0)

turtle.done()












