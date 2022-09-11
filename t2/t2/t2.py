import turtle
import math

bob = turtle.Turtle()
bob.color("blue","red")
bob.speed(10)

for i in range(2000):
    bob.forward(math.sin(i/10)*25)
    bob.left(i%200)




turtle.done()