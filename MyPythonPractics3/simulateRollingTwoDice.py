import random

target_sum = int(input("Enter the target sum: "))
while True:
    roll1 = random.randint(1, 6)
    roll2 = random.randint(1, 6)
    print(f"Rolled: {roll1} + {roll2} = {roll1 + roll2}")
    if roll1 + roll2 == target_sum:
        break

# Simulate Rolling Two Dice