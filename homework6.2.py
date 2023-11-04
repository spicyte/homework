numbers = list(range(1, 101))
result_list = []

i = 0
while i < len(numbers):
    if numbers[i] % 7 == 0 and numbers[i] % 5 != 0:
        result_list.append(numbers[i])
    i += 1

print(result_list)
