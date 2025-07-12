# Simple inheritance

# Base class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound")

# Derived class
class Dog(Animal):
    def speak(self):
        print(f"{self.name} barks")

# Object creation
animal = Animal("Cat")
animal.speak()  
dog = Dog("Tommy")
dog.speak()     # Output: Tommy barks
# Output: Cat makes a sound
# Method overriding example
# Both Animal and Dog have a method called speak()
# The Dog class overrides the speak() method of the Animal class
# When you call dog.speak(), Python runs the Dog version (not the parent one)
# This is runtime polymorphism: method called depends on the object



