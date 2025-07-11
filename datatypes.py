lst=[1,2,3]
my_str="abc"
my_int=1
print(type(lst))
#list is also class in python
print(type(my_str))
#string is also class in python
print(type(my_int))
#int is also class in python
#lst.clear
#print(list)
#lst.count
#print(lst)


my_str_obj = my_str.capitalize()
print(my_str_obj)
a = 'x' 
b = 'y'
print(a+b)
# here `my_str_obj` is the new string object (object)
# class is `str` (not my_str) — because all strings are instances of Python's built-in `str` class
# `capitalize()` is a method from the `str` class
# it creates a new string and stores it in `my_str_obj`
