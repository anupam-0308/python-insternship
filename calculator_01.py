while True:
 print(""""
      choose the options below for operations
      1.addition
      2.subtraction
      3.multiplication
      4.division
      5.for converting degree celcious into degree fahrenheit
      6.for converting meter to cm
      7.for exiting
      """)
 choice=input ("enter your choice :")
 if choice=="1":
  num1=int(input("enter the first number :"))
  num2=int(input("enter the second number :"))
  print(f'addition is :',num1+num2)

 elif choice=="2":
  num1=int(input("enter the first number :"))
  num2=int(input("enter the second number :"))
  print(f'subtraction is :',num1-num2)

 elif choice=="3":
  num1=int(input("enter the first number :"))
  num2=int(input("enter the second number :"))
  print(f'multiplication is :',num1*num2)

 elif choice=="4":
  num1=int(input("enter the first number :"))
  num2=int(input("enter the second number :"))
  print(f'division is :',num1/num2)

 elif choice=="5":
  num1 =float(input("enter the temperature in celcious :"))
  num2=((num1*1.8)+32)
  print("your temperature in fahrenheit is",num2)

 elif choice=="6":
  num1=int(input("enter the number in meters :")) 
  print("your number in cm is",num1*100)
     
 elif choice=="7":
  print("Thankyou")
  break
     
 else :
  print("invalid")
