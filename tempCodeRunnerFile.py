

print("<-------------| Your Cards |--------------->")
print(f"| | \t\t {user_card} \t\t | |")
print("<------------------------------------------>")


choice = input("Do you want extra card? (y / n): ")

if (choice.lower() == "y"):
    
    Comp_Card_Extra_Sum
    print("<-------------| Your Cards |--------------->")
    print(f"| | \t\t {user_card} \t\t | |")
    print("<------------------------------------------>")
    print(f"Your sum of card after new card is {user_sum}")
    
else:
    print(f"Your sum of card is {user_sum}")