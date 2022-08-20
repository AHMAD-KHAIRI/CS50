# create a python program that simulates the flipping of a coin

# first import the random library
# import random

# if we don't want to add the random library, we can use from and import only the function that we want
# this means we don't need to call random.choice but just call the function choice
from random import choice

# random.choice(seq): Return a random element from the non-empty sequence seq.
# create a list: "heads" or "tails" and save it in a variable
# coin = random.choice(["head", "tails"])
coin = choice(["head", "tails"])

print(coin)
