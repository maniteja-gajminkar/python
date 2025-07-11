#Create a Python class named Student that takes name, roll_no, and grade as input during object creation.
#Add a method display_info() that prints the student's details.

class student:
    #Without self	Just a local temp value — gone after function ends
    #With self	Saved permanently in the object’s memory
    #self.name = name	Save the passed-in name to the object
    #self.name in methods	Access the saved name
    def __init__(self,name,rollno,grade):
     #What is __init__()?,It’s called a constructor.Runs automatically when you create an object.

    ##It’s used to initialize the object’s data,When you create an object, 
    # __init__() sets up the values you want that object to start with.    
        self.name = name
        self.rollno = rollno
        self.grade = grade
    def display_info(self):
        print(f"Name is {self.name},Rollno is {self.rollno}, Gradeis {self.grade}")

#student = student("teja", "1","a")
#dont create obj and calssname samea s it overwrites class w ecannot create second object for class
#new_stu = student("ram", "2", "b")  # ❌ Error, because 'student' is now an object, not a class!

student1 = student("teja", "1","a")
student1.display_info()
