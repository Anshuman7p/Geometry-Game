import turtle

#create a canvas instance
myturtle = turtle.Turtle()

#go to a certain coordinate
myturtle.penup()
myturtle.goto(50, 75)

myturtle.pendown()
myturtle.forward(100) # move 100 Pixel
myturtle.left(90)     # turn 90 degree left
myturtle.forward(200)
myturtle.left(90)
myturtle.forward(100)
myturtle.left(90)
myturtle.forward(200)

turtle.done()