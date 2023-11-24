with open('test.txt', 'w') as week:
    weeks = week.write("Hello file world")
print(weeks)

with open('test.txt', 'r') as week_file:
    file = week_file.read()

print(file)