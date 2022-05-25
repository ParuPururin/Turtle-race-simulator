from turtle import Screen
from random import choice
from racer_turtle import RacerTurtle
from time import sleep

# Initial setup
window = Screen()
window.title("What does race mean?")
window.setup(720, 405)  # Aspect ratio 16:9
window.bgcolor("#fef5e7")  # Perhaps a bit gentle color on the eyes

# Variables for our race
colors = ["Red", "Orange", "Gold", "Green", "Darkcyan", "Blue", "Purple"]
names = ["Raphael", "Michelangelo", "Jake", "Pora", "Marina", "Leonardo", "Donatello"]
turtles = list()
past_racers = list()
race_on = True
y_base = -150

# Simpleton algorithm to move and recover stamina on each racer

def move_turtle(the_racer, a_past_racers):
    temp = list()
    not_up_stamina = list()
    last_racer = a_past_racers.pop()  # Remove the last previous racer
    not_up_stamina.append(last_racer)  # Add it on the list to not recover stamina
    the_racer.move()

    if the_racer is a_past_racers[-1]:
        not_up_stamina.append(the_racer)  # If the actual racer has move recently, it won't recover sta
    temp.insert(0, the_racer)
    temp.insert(0, last_racer)

    # Let's recover previous racer stamina
    for turtle in a_past_racers:
        if turtle in not_up_stamina:
            temp.insert(0, turtle)  # The racer will recover stamina on other turn
        else:
            turtle.stamina_up()
            not_up_stamina.append(turtle)  # Racer recovers stamina, it would recover just once per turn
    return temp

# Creating the turtles
for color, name  in zip(colors, names):
    turtle = RacerTurtle(color, name)
    turtle.penup()
    turtle.setpos(x=-350, y=y_base)
    y_base += 50
    turtles.append(turtle)

# Preparing our previous simpleton algorithm
for _ in range(2):
    racer = choice(turtles)
    print(f"{racer.give_name()} has {racer.current_stamina} stamina.")
    racer.move()
    past_racers.append(racer)

# Race Let's Goooooooooooooooo!
while race_on:
    racer = choice(turtles)
    print(f"{racer.give_name()} has {racer.current_stamina} stamina.")
    past_racers = move_turtle(racer, past_racers)
    sleep(0.20)

    # We have a winner
    if racer.xcor() >= 330:
        race_on = False
        print(f"{racer.give_name()} has won!")
        racer.victory_dance()

window.exitonclick()  # I want to close the window
