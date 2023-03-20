# Write your code below this row 👇
n = int(input("Enter the number upto which evens must be add. : "))


sum1 = 0
for i in range(1, n+1):
    if (i % 2 == 0):
        sum1 += i
print(sum1)


# OR


sum2 = 0
for i in range(2, n+1, 2):
    sum2 += i
print(sum2)
