print("Welcome to roller coaster")
height = int(input("What is your height: "))
bill = 0

if height >= 120:
    print("You can ride")
    age = int(input("What is your age: "))
    if age < 12:
        bill = 5
        print(f"You got to pay ${bill}")
    elif age >= 18:
        bill = 12
        print(f"You will pay{bill}")
    elif age > 12:
        bill = 7
        print(f"You will pay ${bill}")
    # picture
    picture = input("Do you want picture: y or n")
    if picture == "y":
        bill += 3

    print(f"Your total bill is ${bill}")


else:
    print("Can't ride")
