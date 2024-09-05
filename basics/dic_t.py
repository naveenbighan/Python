# marks={}
# a= (input("enter subject name:"))
# x= int(input("enter no.:"))
# marks.update({a:x})
# a= (input("enter subject name:"))
# x= int(input("enter no.:"))
# marks.update({a:x})
# a= (input("enter subject name:"))
# x= int(input("enter no.:"))
# marks.update({a:x})

# print(marks)


dict={x:x*2 for x in range(2,20)}
print(dict)

tup=(x*2 for x in range(10))
hp= tuple(tup)
print(hp)

nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat_list = [item for subitem in nested_list for item in subitem ]
print(flat_list)
