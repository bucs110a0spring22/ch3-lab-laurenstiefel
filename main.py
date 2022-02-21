import turtle               #1. import modules
import random

#Part A
window = turtle.Screen()       # 2.  Create a screen
window.bgcolor('lightblue')

michelangelo = turtle.Turtle()    # 3.  Create two turtles
leonardo = turtle.Turtle()
michelangelo.color('orange')
leonardo.color('blue')
michelangelo.shape('turtle')
leonardo.shape('turtle')

michelangelo.up()          # 4.  Pick up the pen so we don’t get lines
leonardo.up()
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

## 5. your code goes here
x=random.randrange(1,101)
leonardo.forward(x)
michelangelo.forward(x)

michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

for distance in range(10):
  y=random.randrange(1,11)
  michelangelo.forward(y)
  z=random.randrange(1,11)
  leonardo.forward(z)
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

  

# Part B - complete part B here
list=[3,4,6,9,12]
michelangelo.down()
for side in (3,4,6,9,12):
  for shape in range (side):
    angle=(360/side)
    michelangelo.forward(30)
    michelangelo.left(angle)
  michelangelo.clear()    
  

window.exitonclick()
