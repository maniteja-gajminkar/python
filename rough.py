from oops_proj import chatbook

user1 = chatbook()
#print(user1._chatbook__name)
#print(user1.get_name())
#user1.set_name("agent x")
#print(user1.get_name())
print(user1.id)


chatbook.set_id(10)
user2 = chatbook()
print(user2.id)

user3 = chatbook()
print(user3.id)

#user3 = chatbook()
#print(user3.id)
#Can the object be named user1, even if it was named obj in oops_proj.py?
#✅ Yes — object names are local to the file (script).

#lst = [1,2,3]

#function
#a1 = len(lst)
#print(a1)

#method
#user1 = chatbook()
#user1.sendingmsg()

#method is also a function wchich is writte in class
# ✅ Function:
# A function is a block of code that performs a task and is defined using 'def'.
# It is not tied to any class or object unless manually passed.

#def greet():
#    print("Hello!")

#greet()  # Function call


# ✅ Method:
# A method is also a function, BUT it is defined **inside a class**
# and is associated with an object (via 'self').

#class MyClass:
#    def my_method(self):  # This is a method
#        print("Hello from a method!")

#obj = MyClass()
#obj.my_method()  # Method call — requires object

# ✅ Summary in comments:
# Function → Standalone, doesn't depend on object
# Method → Belongs to a class, works through object using 'self'
# ✅ A method is just a function that's called on an object (like user1)
