import turtle
import time

turtle.forward(100) #imprime una flecha con la punta siempre hacía la derecha y se mueve 100 píxeles
time.sleep(1) #hace que no se cierre la pantalla inmediatamente
turtle.right(90) # el 90 son los grados
time.sleep(1) #hace que no se cierre la pantalla inmediatamente
turtle.backward(50) # el 50 son los prixeles
time.sleep(1) #hace que no se cierre la pantalla inmediatamente
turtle.left(90)
time.sleep(1) #hace que no se cierre la pantalla inmediatamente
turtle.circle(150)
time.sleep(1) #hace que no se cierre la pantalla inmediatamente
turtle.penup()
turtle.setx(-100)
turtle.sety(-100)
turtle.pendown()
turtle.circle(30)
