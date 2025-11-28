print("there are only 3 tickets left !")
age = int(input("Enter your age : "))
tck = int(input("How many ticket do you want : "))
if age > 18:
    if tck > 3:
        print("You can watch this movie")
        print("But you can only have 3 tickets")
        print("collect your ticket")
    else:
        print("You can watch this movie")
        print("collect your ticket")
elif age > 15:
    if tck > 3:
        print("You can watch this movie with your parents")
        print("But you can only have 3 tickets")
        print("collect your ticket")
    else:
        print("You can watch this movie with your parents")
        print("collect your ticket")
else:
    print("Sorry !! you can not watch this movie")