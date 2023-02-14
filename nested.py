from turtle import *
speed(0)

fillcolor('blue')
pencolor('red')
side = 6
pu()
goto(-150, 200)
pd()
for i in range(side):
    fd(150)
    for i in range(side): 
        fd(100)
        for i in range(side):
            fd(100)
            begin_fill()
            dot(10)
            rt(360/side)
        lt(360/side)
    end_fill()
    rt(360/side)    
    
hideturtle()
mainloop()
