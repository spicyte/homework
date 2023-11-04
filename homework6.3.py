import random

random_number1 = []
count = 0
while count < 10:
    random_number1.append(random.randint(1, 100))

print("Список номер один: ", random_number1)

random_number2 = []
count = 0
while count < 20:
    random_number2.append(random.randint(1, 100))
print("Список номер два: ", random_number2)

random_number3 = random_number2 + random_number1
print(random_number3)