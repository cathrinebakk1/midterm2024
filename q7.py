import random
random_numbers = []
for i in range(10):
    random_numbers.append(random.randint(1, 100))

# Replacing numbers greater than 80 with their negative value
for i in range(len(random_numbers)):
    if random_numbers[i] > 80:
        random_numbers[i] = -random_numbers[i]

# Printing the modified list
print(random_numbers)
