class WorkHoursCounter:
    def __init__(self):
        self.tasks = []
        self.total_hours = 0

    def add_task(self, description, hours):
        self.tasks.append({"description": description, "hours": hours})
        self.total_hours += hours

    def __iter__(self):
        self.current_task = 0
        return self

    def __next__(self):
        if self.current_task < len(self.tasks):
            task = self.tasks[self.current_task]
            self.current_task += 1
            return f"{task['description']} - {task['hours']} годин"
        else:
            raise StopIteration

    def productivity_summary(self):
        print(f"Загальний час витрачений на роботу: {self.total_hours} годин")
        print("Завдання:")
        for task in self.tasks:
            print(f"- {task['description']}: {task['hours']} годин")

if __name__ == "__main__":
    counter = WorkHoursCounter()

    counter.add_task("Написати статтю", 2)
    counter.add_task("Вивчити новий пакет", 1.5)
    counter.add_task("Підготувати презентацію", 3)

    for task in counter:
        print(task)


    counter.productivity_summary()
