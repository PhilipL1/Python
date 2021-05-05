from datetime import date
import random
class Animal:
    def __init__(self, name, date_of_birth):
        self.name = name
        self.date_of_birth = date_of_birth
    def get_age(self):
        return date.today().year - self.date_of_birth.year
    def breathe(self):
        return f"{self.name} takes a breath"
    def eat(self, food):
        message = f"{self.name} eats {food}"
        if random.randint(0,1):
            return message + " and they love it!"
        else:
            return message + " and they hate it!"
class Dog(Animal):
    # constructor
    def __init__(self, name, date_of_birth, breed, energy):
        super().__init__(name, date_of_birth)
        self.breed = breed
        self.energy = energy
    
    def bark(self):
        if self.energy > 5:
            return f"{self.name} goes bark!"
        else:
            return f"{self.name} boofs gently!"
john = Animal("John", date(2010,12,15))
spike = Dog("Spike", date(2019,3,16), "pitbull", 6)
print(john.get_age())
print(spike.get_age())
print(spike.bark())
print(spike.eat("apple"))
