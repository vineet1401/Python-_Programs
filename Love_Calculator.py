# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
combine_name = name1.lower() + name2.lower()

true_count = combine_name.count(
    "t") + combine_name.count("r") + combine_name.count("u") + combine_name.count("e")
love_count = combine_name.count(
    "l") + combine_name.count("o") + combine_name.count("v") + combine_name.count("e")

score = int(str(true_count) + str(love_count))

if (score < 10 or score > 90):
    print(f"Your score is {score}, you go together like coke and mentos.")
elif (40 <= score <= 50):
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
