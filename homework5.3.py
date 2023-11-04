import random

string = input("Уведiть стрiчку: ")

for i in range(5):
    random_string = ''.join(random.choice(string) for i in range(len(string)))
    print(random_string)


