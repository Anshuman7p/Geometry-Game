from random import randint
import turtle

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def fall_in_ractangle(self, rectangle):
        if rectangle.lwrleft.x < self.x < rectangle.uprright.x and rectangle.lwrleft.y < self.y < rectangle.uprright.y:
            return True
        else:
            return False

class Rectangle:
    
    def __init__(self, lwrleft, uprright):
        self.lwrleft = lwrleft
        self.uprright = uprright
        
    def area(self):
        return(self.uprright.x - self.lwrleft.x) * (self.uprright.y - self.lwrleft.y)
    
    
class GuiRectangle(Rectangle):
    
    def draw(self, canvas):
        #go to a certain coordinate
        canvas.penup()
        canvas.goto(self.lwrleft.x, self.uprright.y)

        canvas.pendown()
        canvas.forward(self.uprright.x - self.lwrleft.x) # move 100 Pixel
        canvas.left(90)     # turn 90 degree left
        canvas.forward(self.uprright.y - self.lwrleft.y)
        canvas.left(90)
        canvas.forward(self.uprright.x - self.lwrleft.x)
        canvas.left(90)
        canvas.forward(self.uprright.y - self.lwrleft.y)

        
class GuiPoint(Point):
    
    def draw(self, canvas, size=5, color='red'):
        canvas.penup()
        canvas.goto(self.x, self.y)
        canvas.pendown()
        canvas.dot(size, color)

 
#create rectangle object
rectangle = GuiRectangle(
    Point(randint(0,400), randint(0,400)),
          Point(randint(10,400), randint(10,400)))


# print rectangle coordinates
print("Rectangle coordinate: ",
      rectangle.lwrleft.x,",",
      rectangle.lwrleft.y,"and",
      rectangle.uprright.x,",",
      rectangle.uprright.y,)


# gets points and area from users
user_point = GuiPoint(float(input("Guess X: ")),
                   float(input("Guess Y: ")))

user_area = float(input("Guess Area: "))


# print out the game result
print("Your point was inside rectangle: ",
      user_point.fall_in_ractangle(rectangle))

print("Your area was off by: ",
      rectangle.area() - user_area)

   
myturtle = turtle.Turtle()
rectangle.draw(canvas=myturtle)
user_point.draw(canvas=myturtle)

turtle.done()