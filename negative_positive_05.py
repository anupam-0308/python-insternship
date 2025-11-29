def number_checker():
    
    print("Number Checker ")

user_input = input("Please enter a number: ")
number = float(user_input)
        
while True:       
    if number > 0:
        print("\n The number is positive.")
        break
    elif number < 0:
        print("\n The number is negative.")
        break
    elif number == 0:
        print("\n The number is zero.")
        break
    else:
     
     print("\n❌ Invalid input. That was not a valid number. Please try again.")

     break

if __name__ == "__main__":
    number_checker()

