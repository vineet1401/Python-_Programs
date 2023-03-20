# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
S_pizza = 15
M_pizza = 20
L_pizza = 25
S_pepo = 2
M_L_pepo = 3
E_cheese = 1

bill = 0

if (size == "S"):
    bill += S_pizza
    if (add_pepperoni == "Y"):
        bill += S_pepo
    else:
        pass
    if (extra_cheese == "Y"):
        bill += E_cheese
    else:
        pass
elif (size == "M"):
    bill += M_pizza
    if (add_pepperoni == "Y"):
        bill += M_L_pepo
    else:
        pass
    if (extra_cheese == "Y"):
        bill += E_cheese
    else:
        pass
else:
    bill += L_pizza
    if (add_pepperoni == "Y"):
        bill += M_L_pepo
    else:
        pass
    if (extra_cheese == "Y"):
        bill += E_cheese
    else:
        pass

print(f"Your final bill is: ${bill}.")
