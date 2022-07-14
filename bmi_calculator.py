# This program calculates the Body Mass Index of a person and prints the result 
# following the conditions in the if statements below.
# Note here that the program takes in the height and weight as floating point numbers
# and rounds up the result to a whole number

height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
result = round(weight / height ** 2)

if result < 18.5:
    result_statement = ("you are underweight.")
elif result < 25:
    result_statement = ("you have a normal weight.")
elif result < 30:
    result_statement = ("you are slightly overweight.")
elif result < 35:
    result_statement = ("you are obese.")
elif result > 35:
    result_statement = ("you are clinically obese.")

print(f"Your BMI is {result}, {result_statement}")