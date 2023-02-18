import json

def load_data():
    base_info = {
        "Raphael": {
            "color": "Red",
            "wins": 0
        },
        "Michelangelo": {
            "color": "Orange",
            "wins": 0
        },
        "Jake": {
            "color": "Gold",
            "wins": 0
        },
        "Pora": {
            "color": "Green",
            "wins": 0
        },
        "Marina": {
            "color": "Darkcyan",
            "wins": 0
        },
        "Leonardo": {
            "color": "Blue",
            "wins": 0
        },
        "Donatello": {
            "color": "Purple",
            "wins": 0
        }
    }

    try:
        with open("./info.json") as f:
            base_info = json.load(f)
    except FileNotFoundError:
        print("Data not found!\nWhere're your turtles?")
        with open("./info.json", "w") as f:
            json.dump(base_info, f)
        print("Data created!")
    return base_info

def save_data(updated_data):
    with open("./info.json", "w") as f:
            json.dump(updated_data, f)

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
