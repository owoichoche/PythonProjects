# This program calculates one's life in weeks.
# It tells us how many days, weeks and months we have left if we live until 90 years old.
# The program will take your current age as the input and output a message with our time left.

age = input("What is your current age? ")

# number of years left = 90 - age

age = int(age)
x = (90 - age) * 365 #number of days left
y = (90 - age) * 52 #number of weeks left
z = (90 - age) * 12 #number of months left

print(f"You have {x} days, {y} weeks, and {z} months left.")



