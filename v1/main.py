from turtle import Turtle, Screen
from random import randint, choice

# Initial setup
window = Screen()
window.title("What does race mean?")
window.setup(720, 405)  # Aspect ratio 16:9

# Variables for our race
colors = ["Red", "Orange", "Gold", "Green", "Darkcyan", "Blue", "Purple"]
turtles = list()
race_on = True
y_base = -150

# Creating the turtles
for color in colors:
    turtle = Turtle(shape="turtle")
    turtle.color(color)
    turtle.penup()
    turtle.setpos(x=-350, y=y_base)
    y_base += 50
    turtles.append(turtle)

# Race Let's Goooooooooooooooo!
while race_on:
    steps = randint(2, 6)
    racer = choice(turtles)
    racer.forward(steps)

    # We have a winner
    if racer.xcor() >= 330:
        race_on = False
        print(f"{racer.pencolor()} has won!")

window.exitonclick()  # I want to close the window
