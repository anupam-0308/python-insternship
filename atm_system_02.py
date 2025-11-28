balance = 5000
correct_pin = 69

while True:
    pin_attempts = 0

    while pin_attempts < 3:
        pin = int(input("Enter your PIN: "))

        if pin == correct_pin:
            x = int(input("Enter the amount you want to withdraw: "))

            if x > balance:
                print("Insufficient balance")
            else:
                balance -= x
                print("Your remaining balance is:", balance)

            break  # exit PIN loop

        else:
            print("Wrong PIN")
            pin_attempts += 1

    if pin_attempts >= 3:
        print("Blocked")
        break

    continue_choice = input("Do you want to continue (yes/no)? ").strip().lower()

    if continue_choice != "yes":
        break
