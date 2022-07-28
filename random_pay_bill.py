#This program takes names as input and 
# selects any at random to pay the bill
import random

name_string = input("Give me everybody's names, seperated by a comma: ")
names = name_string.split(", ")
#Get the total number of items in the list
num_items = len(names)

random_choice = random.randint(0, num_items - 1)
person_who_will_pay = names[random_choice]
print(person_who_will_pay + " is going to buy the meal today")

