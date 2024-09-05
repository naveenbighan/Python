# # 
# def num():
#   x=int(input("enter a no:"))
#   if x%2==0:
#     print("no is even")
#   else:print("no.is odd")
# num()

def outer_function():
    def nested_function():
        return "Hello from the nested function!"
    
    return nested_function  # Returning the nested function

# Assign the nested function to a variab
nested = outer_function()
print(nested())

# Now you can use the nested function outside the outer function
  # Output: Hello from the nested function!


# class Student:
#     def __init__(self, name, age,section):
#         self.name=name
#         self.age=age
#         self.section=section
#         print(f"{self.name},{self.age},{self.section}")
# student= Student("naveen",25,"A")


# x= "this is gloabal scope msg"

# def outer():
#     #  x="this is local scope msg"
#     def inner():
#         #  x="this is local scope msg"
       
#          print(x)
#     inner()
# outer()

def f1():
    x=88
    def f2():
        print(x)
    return f2

hello =f1()
hello()

    
