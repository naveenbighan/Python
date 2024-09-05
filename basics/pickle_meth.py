import pickle
# list= ["lemon","ginger","garlic","potato"]

# with open("naveen.txt","rb") as file:
#     data= file.read()
#     print(data)


with open("naveen.txt","rb") as file:
    data= pickle.load(file)
    
    
    
    print(f"{id(data)}")
