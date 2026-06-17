import turtle #built in graphics library used for drawing shapes

t=turtle.Turtle() #creats a drawing object 
s=turtle.Screen() #creates the windows screen where the art will be display 
s.bgcolor("black") #background color
t.speed(0) #object's animation speed, 0 for fastest
turtle.tracer(3,0)
t.color("#D7CCC8")

for i in range(400):
    t.forward(i)
    t.left(170)
    t.forward(i)
    t.left(45)
turtle.done()

