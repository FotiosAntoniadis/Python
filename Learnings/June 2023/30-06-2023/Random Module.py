import random

# Pick a number from 1 to 6 (like a dice)
x = random.randint(1, 6)
#          ^     ^
#       random + int

print(x)

print("---------------------")

# Print a random Float number
y = random.random()

print(y)

print("---------------------")

# Print a random value from a list
game = ["rock", "paper", "scissors"]

z = random.choice(game)
print(z)

print("---------------------")

# Shuffle a list (yeah I know 1 = A)
cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, "J", "Q", "K", "A"]

random.shuffle(cards)

print(cards)

# 30/06/23