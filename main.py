class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        return "Animal sound"

    def info(self):
        return f"Name: {self.name}, Age: {self.age}"

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

bobik = Dog("Bobik", 3)
murka = Cat("Murka", 2)

print(bobik.info())
print(bobik.speak())
print(murka.info())
print(murka.speak())
