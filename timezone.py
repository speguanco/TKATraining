import time
import turtle
#code to print out clock
curr_time = time.localtime
curr_clock = time.strftime("%H:%M:%S", curr_time)

#print result
print(curr_clock)

star = turtle.Turtle()

star.right(75)
star.forward(100)

for i in range(4):
    star.right(144)
    star.forward(100)

turtle.done()

print(curr_time)
