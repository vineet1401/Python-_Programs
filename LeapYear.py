year = int(input("Which year do you want to check? "))


# Write your code below this line 👇
if (year % 4 == 0):
    if (year % 100 == 0):
        if (year % 400 == 0):
            print("Leap year.")
        else:
            print("Not a leap year.")
    else:
        print("Leap year")
else:
    print("Not a leap year")

# Write your code below this line 👇
if ((year % 4 == 0) and (year % 100 == 0) and (year % 400 == 0)):
    print("Leap year")
elif ((year % 4 == 0) and (year % 100 != 0)):
    print("Leap year")
else:
    print("Not a leap year")
