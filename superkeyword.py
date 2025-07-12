#base class
class Animal:
    def __init__(self):
        self.name = "Buddy"

    def speak(self):
        print(f"{self.name} makes a sound")        

#Derived class
class Dog(Animal):
    def __init__(self,bread):
        super().__init__()
        self.bread = bread
    def speak(self):
        super().speak() #calls the base method
        print(f"{self.name} barks, its a {self.bread}")
dog = Dog("Golden Retriever")
dog.speak()

#here super() will call the parent class methods and attributes