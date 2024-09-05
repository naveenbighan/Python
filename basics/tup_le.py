# my_tuple=("c","d","A","A","B","B","A")

# a=my_tuple.index("B")
# print(a)

arr = [1,2,3,4,5,6,7,8,9]
ind=arr[0]
arr[0]=arr[len(arr)-1]
print(arr)
arr[len(arr)-1]=ind
print(arr)



# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True
# print(is_prime(int(input("check no. prime or not:"))))




def reversed(s):
    reversed_str=""
    for i in s:
        reversed_str=i+reversed_str
    return reversed_str
a= "hello"
print(reversed(a))



text= "hello world"
vowels= "AEIOUaeiou"

for char in text:
    if char in vowels:
        print(char)
        
str="hello guys"
str2=""
for i in str:
    str2= i+str2
print(str2)