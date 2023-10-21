import random


class Human:
    def __init__(self, name="Human", home=None, job=None, car=None, animal=None):
        self.name = name
        self.money = 100
        self.gladness = 50
        self.satiety = 50
        self.job = job
        self.home = home
        self.car = car
        self.animal = animal

    def get_home(self):
        self.home = House()

    def get_animal(self):
        pass

    def get_car(self):
        self.car = Auto(brand_of_car)

    def get_job(self):
        if self.car.drive():
            pass
        else:
            self.to_repair()
            return
        self.job = Job(job_list)

    def eat(self):
        if self.home.food <= 0:
            self.shopping("food")
        else:
            if self.satiety >= 100:
                self.satiety = 100
                return
            self.satiety += 5
            self.home.food -= 5

    def work(self):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                self.shopping("fuel")
                return
            else:
                self.to_repair()
                return
            self.money += self.job.salary
            self.gladness -= self.job.gladness_less
            self.satiety -= 4

    def shopping(self, manage):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                manage("fuel")
            else:
                self.to_repair()
                return
        if manage == "fuel":
            print("I bought fuel")
            self.money -= 100
            self.car.fuel += 100
        elif manage == "food":
            print("I bought food")
            self.money -= 50
            self.home.food += 50
        elif manage == "delicacies":
            print("Delicacies!")
            self.gladness += 10
            self.satiety += 2
            self.money -= 15

    def chill(self):
        self.gladness += 10
        self.home.mess += 5

    def clean_home(self):
        self.gladness -= 5
        self.home.mess = 0

    def to_repair(self):
        self.car.strenght += 100
        self.money -= 50

    def play_with(self):
        self.gladness +=10
        self.money -= 10

    def days_indexes(self, day):
        day = f" Today the {day} of {self.name}'s life"
        print(f"{day:=^50}", "\n")
        human_indexes = self.name + "'s indexes"
        print(f"{human_indexes: ^50}", "\n")
        print(f"Money - {self.money}")
        print(f"Satiety - {self.satiety}")
        print(f"Gladness - {self.gladness}")
        home_indexes = "Home indexes"
        print(f"{home_indexes: ^50}", "\n")
        print(f"Food - {self.home.food}")
        print(f"Mess - {self.home.mess}")
        car_indexes = f"{self.car.brand}car indexes"
        print(f"{car_indexes: ^50}", "\n")
        print(f"Fuel - {self.car.fuel}")
        print(f"Strenght - {self.car.strenght}")
        pet_indexes = f"{self.animal.types}pet indexes"
        print(f"{pet_indexes: ^50}", "\n")
        print(f"Energy - {self.animal.energy}")
        print(f"Enjoyment - {self.car.enjoyment}")

    def is_alive(self):
        if self.gladness < 0:
            print("Depression")
            return False
        if self.satiety < 0:
            print("Dead...")
            return False
        if self.money < - 500:
            print("Bankrupt...")
            return False

    def live(self, day):
        if self.is_alive() == False:
            return False
        if self.home is None:
            print("Settled in the house")
            self.get_home()
        if self.car is None:
            self.get_car()
            print(f"I bought a car {self.car.brand}")
        if self.job is None:
            self.get_job()
            print(f"I don't have a job , I'm going to get a job {self.job.job} with salary {self.job.salary} ")
        self.days_indexes(day)
        dice = random.randint(1, 4)
        if self.satiety < 20:
            print("I'll go eat")
            self.eat()
        elif self.gladness < 20:
            if self.home.mess > 15:
                print("I want to rest, but there is so mess..\ I need to clean my house")
                self.clean_home()
            else:
                print("Let's chill")
                self.chill()
        elif self.money < 0:
            print("Start working")
            self.work()
        elif self.car.strenght < 15:
            print("I need to repair my car")
            self.to_repair()
        elif dice == 1:
            print("Let's chill")
            self.chill()
        elif dice == 2:
            print("Start working")
            self.work()
        elif dice == 3:
            print("Cleaning time")
            self.clean_home()
        elif dice == 4:
            print("Time for treats")
            self.shopping(manage = "delicacies")


class Auto:
    def __init__(self, brand_list):
        self.brand = random.choice(list(brand_list))
        self.fuel = brand_list[self.brand]["fuel"]
        self.strenght = brand_list[self.brand]["strenght"]
        self.consumption = brand_list[self.brand]["consumption"]


    def drive(self):
        if self.strenght > 0 and self.fuel >= self.consumption:
            self.fuel -= self.consumption
            self.strenght -= 1
            return True
        else:
            print("The car can't move")
            return False

    def animal(self):
        if self.enjoyment > 0 and self.energy >= self.consumption:
            self.energy -= self.consumption
            self.enjoyment -= 1
            return True
        else:
            print("Your pet isn't in happy mood")
            return False


class Animal:
    def __init__(self, list_of_animal):
        self.list_of_animal = random.choice(list(types_of_animal))
        self.energy = list_of_animal[self.types]["energy"]
        self.enjoyment = list_of_animal[self.types]["enjoyment"]
        self.consumption = list_of_animal[self.types]["consumption"]


class House:
    def __init__(self):
        self.mess = 0
        self.food = 0


brand_of_car = {
    '宝马 BMW': {"fuel": 100, "strenght": 100, "consumption": 6},
    '本田 Honda': {"fuel": 50, "strenght": 40, "consumption": 10},
    '沃尔沃 Volvo': {"fuel": 70, "strenght": 150, "consumption": 8}}

types_of_animal = {
    'Dog': {"energy": 130, "enjoyment": 230, "consumption": 26},
    'Cat': {"energy": 150, "enjoyment": 80, "consumption": 9},
    'Parrot': {"energy": 90, "enjoyment": 110, "consumption": 4}}


job_list = {
    "Java开发人员 Java developer": {"salary": 50, "gladness_less": 10},
    "Python开发人员 Python developer": {"salary": 40, "gladness_less": 3},
    "C++开发人员 C++ developer": {"salary": 45, "gladness_less": 25},
    "Rust 开发人员 Rust developer": {"salary": 70, "gladness_less": 1}}


class Job:
    def __init__(self, job_list):
        self.job = random.choice(list(job_list))
        self.salary = job_list[self.job]["salary"]
        self.gladness_less = job_list[self.job]["gladness_less"]

nick = Human(name="Nick")
for day in range(1, 8):
    if nick.live(day):
        break