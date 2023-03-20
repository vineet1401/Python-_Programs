number = int(input("Enter the number : "))
print ("------Number in Weird Algorithm-------")
print(number, end = " ")
cond = True
while (cond):
    if (number%2 == 0):
        number //= 2
        print(number, end=" ")
    elif (number == 1):
        break
    else:
        number = (number * 3) + 1
        print(number, end=" ")
        
