#simple inheritance

#Base class
class Animal:
    def __init__(self,name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound")
#Derived class
class Dog(Animal):
    def __init__(self):
        self.behaviour =  "friendly"
    def speak(self):
        print(f"dog barks.he is {self.behaviour}")
#animal = Animal("cat")
#animal.speak()

dog = Dog()
dog.speak()
    
    
