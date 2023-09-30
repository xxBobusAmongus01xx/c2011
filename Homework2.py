import random


class Animal:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.power = 0
        self.alive = True

    def eat(self):
        print("It's time to eat")
        self.power += 0.12
        self.gladness -= 3

    def sleep(self):
        print("I going to sleep")
        self.gladness += 3

    def play(self):
        print("It's playing time")
        self.gladness += 5
        self.power += 0.1

    def is_alive(self):
        if self.power < -0.5:
            print("Passed Away (Died)")
            self.alive = False
        elif self.gladness <= 0:
            print("Sad")
            self.alive = False

    def end_of_day(self):
        print(f"Gladness = {self.gladness}")
        print(f"Power = {round(self.power, 2)}")

    def live(self, day):
        day = "Day" + str(day) + "of" + self.name + "life"
        print(f"{day:=^50}")
        live_cube = random.randint(1, 3)
        if live_cube == 1:
            self.eat()
        elif live_cube == 2:
            self.sleep()
        elif live_cube == 3:
            self.play()
        self.end_of_day()
        self.is_alive()


dog = Animal(name="Dog")
for day in range(365):
    if not dog.alive:
        break
    dog.live(day)