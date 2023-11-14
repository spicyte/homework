my_list = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
my_dict = {"Sunday": 1, "Monday": 2, "Tuesday": 3, "Wednesday": 4, "Thursday": 5, "Friday": 6, "Saturday": 7}
my_dict = {"Sunday": 1, "Monday": 2, "Tuesday": 3, "Wednesday": 4, "Thursday": 5, "Friday": 6, "Saturday": 7}

keys = list(my_dict.keys())
values = list(my_dict.values())

keys.reverse()
values.reverse()

reversed_dict = dict(zip(keys, values))

print(reversed_dict)
