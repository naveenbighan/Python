import random
import string

char=string.ascii_letters + string.digits + string.punctuation
length=int(input("enter numbers "))
password=""
for i in range(length):
    password += random.choice(char)
    
print("the password is:", password)