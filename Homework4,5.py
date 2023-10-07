import random


class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.money = 50
        self.progress = 0
        self.alive = True

    def study(self):
        print(" Time to study")
        self.progress += 0.12
        self.money -= 1
        self.gladness -= 3

    def sleep(self):
        print("I will sleep")
        self.gladness += 3

    def chill(self):
        print("Rest time")
        self.gladness += 5
        self.progress -= 0.1

    def work(self):
        print("Go find some work")
        self.gladness -= 0.4
        self.progress += 0.1
        self.money += 25

    def is_alive(self):
        if self.progress < -0.5:
            print("Cast out..")
            self.alive = False
        elif self.gladness <= 0:
            print("Depresion")
            self.alive = False
        elif self.progress > 5:
            print("Passed externallu...")
            self.alive = False
        elif self.money < -0.1:
            print("Not enough money")
            self.alive = False

    def end_of_day(self):
        print(f"Gladness = {self.gladness}")
        print(f"Progress = {round(self.progress, 2)}")
        print(f"Money = {self.money}")

    def live(self, day):
        day = "Day" + str(day) + "of" + self.name + "life"
        print(f"{day:=^50}")
        live_cube = random.randint(1, 3)
        if live_cube == 1:
            self.study()
        elif live_cube == 2:
            self.sleep()
        elif live_cube == 3:
            self.chill()
        elif live_cube == 4:
            self.work()
        self.end_of_day()
        self.is_alive()


nick = Student(name="Nick")
for day in range(365):
    if nick.alive == False:
        break
    nick.live(day)