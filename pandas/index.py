import pandas as pd



#Create a simple Pandas Series from a list:

# a = [1, 7, 2]

# myvar = pd.Series(a)

# print(myvar)


#With the index argument, you can name your own labels.
# a = [1, 7, 9, 11, 15]
# myvar= pd.Series(a, index=["A","B","C","D","E"])
# print(myvar["E"])

#Create a simple Pandas Series from a dictionary:
calories={"Day1":300,
          "Day2":330,
          "Day3":350}

a = pd.Series(calories)
print(a)


# Create a Series using only data from "day1" and "day2":
print(a[["Day1","Day2"]])  # prints 300 330

              
              
data = {
 "Cars":["BMW", "AUDI" ,"MERCEDES","VOLSWAGON"],
 "Price":[500000, 600000, 700000, 800000]
}

A= pd.DataFrame(data)
print(A.loc[0])








