
# # Write a Python function is_prime(n) that returns
# # True if the number n is prime, and False otherwise.

# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True
# is_prime(5)

# # print table in ywo lines
# # for i in range(1,20):
# #     print(i)

# #find vowels
# # text= "hello world"
# # vowels= "AEIOUaeiou"

# # for char in text:
# #     if char in vowels:
# #         print(char)
    

# #Write a Python function to generate the first n numbers of the Fibonacci sequence.
def fibonacci(n):
    a=0
    b=1
    if n==1:
        print(a)
    else:
     for i in range(2,n):
        c=a+b
        a=b
        b=c
        print(c)
fibonacci(11)

        
             
# def reverse_string(s):
#     if len(s) <= 1:
#         return s
#     else:
#         return reverse_string(s[1:]) + s[0]

# print(reverse_string("hello"))   


#write a class name person give two para in it and display them with another method in class
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print(f"{self.name},{self.age}")

p=person("John",25)
print(p.name)

#list comprehension
x= [a*2 for a in range(1,11)]
print(x)

#dictionary comrehnsion
x={a:a*2 for a in range(1,11)}
print(x)

#How do you find the intersection of two sets in Python? Write a code snippet to demonstrate this.
set1={1,2,3,4,5}
set2={7,8,9,2,5}

intersection = set1 & set2
print(intersection)

#Write a recursive function to calculate the factorial of a number.

def function(n):
    
    if n==0:
       return 1
    else:
       return n*function(n-1)
    
a=function(5)
print(a)