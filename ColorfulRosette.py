# ColorfulRosette.py
# Billy Ridgeway
# Creates a colorful rosette pattern.

import turtle           # Imports turtle graphics.
t = turtle.Pen()        # Creates a new turtle called t.
t.speed(0)              # Sets the pen speed to fast.
t.width(3)              # Sets the width of the pen to 3.
turtle.bgcolor("black") # Sets the background color.

# Ask the user for the number of circles in the rosette, default to 6.
number_of_circles = int(turtle.numinput("Number of circles",
                                       "How many circles in your rosette?", 6))

for x in range(number_of_circles):     # The range equals how many times it will draw a circle.
    t.pencolor('blue')
    t.circle(200)
    t.pencolor('red')
    t.circle(100)
    t.pencolor('yellow')
    t.circle(50)
    t.pencolor('white')
    t.circle(25)
    t.left(360 / number_of_circles)     # How many degrees the circle will shift to the left
                                        # calculated by 360 degrees divided by the number
                                        # of circles.
