def calculator():
  print("---WELCOME TO BASIC CALCULATOR---")

while True:
 
 num1 = float(input("Enter the first number:  "))
 op= input("\nEnter the operation (+, -, *, /) or 'q' to quit: ").strip()
 if op=="q":
     print("\nThanks for using the calculator!")
     break
 num2=float(input("Enter the second number:  " ))
 
 if op=="+":
     print(f"{num1} + {num2} = {num1+num2}")
 elif op=="-":
     print(f"{num1} - {num2} = {num1-num2}")
 elif op=="*":
     print(f"{num1}*{num2}= {num1*num2}")
 elif op=="/":
     if num2 != 0:
      print(f"{num1}/{num2} = {num1/num2}")
 else:
     print("Invalid operation. Please try again.")
     break
     
calculator()
         
         

 
  
