#simple inheritance

#Base class
class Animal:
    def __init__(self,name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound")
#Derived class
class Dog(Animal):
    
    def speak(self):
        print(f"{self.name} barks")
animal = Animal("cat")
animal.speak()

dog = Dog("tiger")
dog.speak()
    
    
