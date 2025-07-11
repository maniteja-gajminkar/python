# initiate a class
class Employee:
    #spcific mehtod/magic method/dunder method constructor
    def __init__(self):
        print( "stated execution atrributes")
        self.id = 123
        self.salary = 50000
        self.designation = "SDE"
        print("atrributes iniitiated")
    
    def travel(self, destination):
        print("travel method caled mannually")
        print(f"Employee is noe travelling to {destination}")

#createan obj/instance of the class
sam = Employee()
print(sam.id)
print(sam.designation)
print(sam.salary)
sam.travel("dubai")
print(type(sam))