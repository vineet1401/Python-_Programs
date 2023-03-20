# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
total_month = 90 * 12
total_days = 365 * 90
total_weeks = 52 * 90

age_month = 12 * int(age)
age_days = 365 * int(age)
age_weeks = 52 * int(age)

print(f"You have {total_days - age_days} days, {total_weeks - age_weeks} weeks, and {total_month - age_month} months left.")
