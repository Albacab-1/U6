import turtle as tt

tt.bgcolor('white')
tt.pensize(3)
tt.speed(6)

for i in range (6):
    for color in ('red', 'magenta','blue', 'cyan', 'green', 'yellow', 'purple'):
        tt.color(color)
        tt.circle(50)
        tt.left(20)

tt.hideturtle()
