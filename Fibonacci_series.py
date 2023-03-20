term = int(input("Enter the number of term : "))
num = 0
num1 = 1

print ("----------Number in Fibonacci Series----------")
if (term <= 0):
    print("Number of term must be greater than 1")
elif (term == 1):
    print(num, end = ' ')
else:
    i = 0
    while (i < term):
        print(num, end=' ')
        number = num + num1
        num = num1
        num1 = number
        i += 1
print()
print("<-------------------------------------------->")