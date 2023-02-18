from random import choice
from racer_turtle import RacerTurtle
import simulation_utils as simu
from turtle import Screen

# Initial setup
window = Screen()
window.title("What does racing means?")
window.setup(720, 405)  # Aspect ratio 16:9
window.bgcolor("#fef5e7")  # Perhaps a bit gentle color on the eyes

# Variables for our race
turtles_data = simu.load_data()
turtles = list()
past_racers = list()
race_on = True
y_base = -150

# Creating the turtles
for name  in turtles_data:
    turtle = RacerTurtle(name, turtles_data[name]["color"])
    turtle.penup()
    turtle.setpos(x=-350, y=y_base)
    y_base += 50
    turtles.append(turtle)

# Preparing our previous simpleton algorithm
for _ in range(2):
    racer = choice(turtles)
    racer.move()
    past_racers.append(racer)

# Race Let's Goooooooooooooooo!
while race_on:
    racer = choice(turtles)
    past_racers = simu.move_turtle(racer, past_racers)

    # We have a winner
    if racer.xcor() >= 330:
        race_on = False
        name = racer.give_name()
        print(f"{name} has won!")
        racer.victory_dance()
        turtles_data[name]["wins"] += 1

simu.save_data(turtles_data)

window.exitonclick()  # I want to close the window
