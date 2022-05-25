from random import randint
from turtle import Turtle
from time import sleep

# Racer inheriting from turtle, with additional attributes
class RacerTurtle(Turtle):
    def __init__(self, color, name):
        super().__init__()  # Calling supercalss' __init__ method, it is need to setup the racer
        self.shape("turtle")
        self.name = name  # Each racer has a different name
        self.color(color)

        # If a racer has more speed, it has less stamina and vice versa.
        speed_factor = randint(0, 2)
        self.racer_speed = 3 + speed_factor
        self.max_stamina = 2 + abs(speed_factor - 2)
        self.current_stamina = self.max_stamina

    def move(self):
        # Each racer need stamina to move, if it has enough, is possible to do an awesome leap

        if self.current_stamina > 0:
            # The racer moves
            steps = randint(1, 3) + self.racer_speed

            if self.current_stamina == self.max_stamina:
                print(f"{self.name} is pumped!")
                steps += 1

            # Try to do an awesome leaps
            if steps > 6:
                print(f"{self.name} try to do a big leap!")
                if self.current_stamina > 1:
                    # Success
                    self.stamina_down()
                    print("Success!")
                else:
                    # Fails, but do a smaller leap
                    steps = 5
                    print("but fails!")

            self.forward(steps)
            self.stamina_down()

        else:
            # Stays to recover 1 point of stamina
            print(f"{self.name} is exahusted")
            self.stamina_up()

    def is_stamina_full(self):
        return self.max_stamina == self.current_stamina

    def stamina_up(self):
        if self.current_stamina < self.max_stamina:
            self.current_stamina += 1

    def stamina_down(self):
        self.current_stamina -= 1

    def victory_dance(self):
        for _ in range(6):
            self.seth(randint(1, 4) * 90 )
            sleep(0.15)

    def give_name(self):
        return self.name


