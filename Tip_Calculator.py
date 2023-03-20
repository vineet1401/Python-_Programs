print("Welcome to the Tip Calclator")
bill = float(input("What was your total bill? $"))
tip = int(input("How much tip you want to give? 10, 12 or 15 : "))
person = int(input("How many person to split the bill? "))

pay = ((bill / person) * (tip / 100)) + (bill / person)
print("Each Person should pay : $" + "{:.2f}".format(pay))
