# initiate a class
class Employee:
    #spcific mehtod/magic method/dunder method constructor
    def __init__(self):
        print(id(self))
        # 'self' represents the current object of the class
# It allows each object to have its own values (like name, age, etc.)
# Without 'self', you cannot store or access data in the object
# It must be the first parameter in every instance method

        #print( "stated execution atrributes")
        self.id = 123
        self.salary = 50000
        self.designation = "SDE"
        #print("atrributes iniitiated")
    
    def travel(self, destination):
        print("travel method caled mannually")
        print(f"Employee is noe travelling to {destination}")
sam = Employee()
sam.name = "samkumar"

#here the moment we create obj all attributes are getting called
print(sam.name)
print(id(sam))
#we can also create attributes outside of the class
shaktiman = Employee()


print(id(shaktiman))
sam.travel("kerala")
# def travel(self, destination)
# → Use when you want to pass different values each time (e.g., "kerala", "delhi", etc.)

# def travel(self)
# → Use when you want a fixed/default message (e.g., always "Delhi")

# self refers to the current object of the class.
# It's automatically passed to every instance method.
# Required to access attributes (self.name) or call other methods (self.travel()) inside the class.
