import random

random_numbers = []
count = 0

while count < 10:
    random_numbers.append(random.randint(1, 100))
    count += 1


print("Список випадкових чисел:", random_numbers)

