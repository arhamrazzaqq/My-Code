class Animal:
    alive = True

class Dog(Animal):
    def speak(self):
        print("WOOFFF")

class Cat(Animal):
    def speak(self):
        print("meooww")
#_____________________
class Car:
    def speak(self):
        print("HONK")
#_____________________
animals = [Dog(), Cat()]

for animal in animals:
    animal.speak()



    