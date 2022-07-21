#This program uses the random module to generate an integer
#whose number determines if the result is Heads or Tails

import random

random_side = random.randint(0, 1)
if random_side == 1:
    print("Heads")
else:
    print("Tails")

