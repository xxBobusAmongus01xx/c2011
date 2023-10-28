import random


class Yaroslav:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.dirty = 0
        self.hunger = 0
        self.alive = True

    def to_study(self):
        print("Time to study")
        self.progress += 0.12
        self.gladness -= 5
        self.dirty += 0.1
        self.hunger += 5

    def to_sleep(self):
        print("I will sleep")
        self.gladness += 3
        self.dirty += 0.3
        self.hunger += 2

    def to_chill(self):
        print("Rest time")
        self.gladness += 5
        self.progress -= 0.1
        self.hunger += 3

    def play_games(self):
        print("I want to play")
        self.progress -= 0.9
        self.gladness +=9
        self.hunger += 2

    def eat(self):
        print("I'm eating")
        self.hunger -= 50
        self.gladness += 3

    def go_for_a_walk(self):
        print("So with friends")
        self.hunger += 1
        self.progress -= 0.5

    def go_to_school(self):
        self.progress += 2
        self.hunger += 0.6

    def is_alive(self):
        if self.progress < -0.5:
            print("Cast out…")
            self.alive = False
        elif self.gladness <= 0:
            print("Depretion")
            self.alive = False
        elif self.progress > 5:
            print("Passed externally...")
            self.alive = False
        elif self.dirty > 1:
            print("I need shower")
            self.alive = False
        elif self.hunger < 100:
            print("I really hungry")
            self.alive = False

    def end_of_day(self):
        print(f"Gladness = {self.gladness}")
        print(f"Progress ={round(self.progress, 2)} ")
        print(f"Hunger = {self.hunger}")
        print(f"Dirty = {self.dirty}")


    def live(self, day):
        day = "Day" + str(day) + "of" + self.name + "life"
        print(f"{day:=^50}")
        live_cube = random.randint(1, 5)
        if live_cube == 1:
            self.to_study()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_chill()
        elif live_cube == 4:
            self.eat()
        elif live_cube == 5:
            self.play_games()
        self.end_of_day()
        self.is_alive()


nick = Yaroslav(name="Yaroslav")
for day in range(366):
    if nick.alive == False:
        break
nick.live(day)
