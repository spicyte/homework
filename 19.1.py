import random

def generate_task():
    tasks = [
        {"description": "Написати про своi мрii", "time_estimate": 120},
        {"description": "Вивчити новий програмний пакет", "time_estimate": 90},
        {"description": "Виконати 30 хвилин фізичних вправ", "time_estimate": 30},
        {"description": "Прочитати книгу", "time_estimate": 60},
        {"description": "Вивчити новий мову програмування", "time_estimate": 120},
        {"description": "Прибрати в кімнаті", "time_estimate": 45},

    ]

    return random.choice(tasks)

def generate_weekly_tasks(num_of_tasks):
    weekly_tasks = []
    for _ in range(num_of_tasks):
        task = generate_task()
        weekly_tasks.append(task)

    return weekly_tasks

if __name__ == "__main__":
    num_of_tasks = 7 
    weekly_tasks = generate_weekly_tasks(num_of_tasks)

    print("Завдання на тиждень:")
    for i, task in enumerate(weekly_tasks, start=1):
        print(f"{i}. {task['description']} (приблизний час виконання: {task['time_estimate']} хвилин)")
