class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True
        

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")


class Dog(Animal):
    def speak(self):
        print("WOOOFF")
class Cat(Animal):
    def speak(self):
        print("meow")
class Mouse(Animal):
    def speak(self):
        print("eee")

dog = Dog("Scooby")
cat = Cat("Garfield")
mouse = Mouse("Mickey")


print(dog.name)
print(dog.is_alive)

dog.eat()
dog.sleep()
dog.speak()