class Boss:
    def __init__(self, id_: int, name: str, company: str):
        self.id = id_
        self.name = name
        self.company = company
        self._workers = []  

    def add_worker(self, worker):
        if isinstance(worker, Worker):
            self._workers.append(worker)
        else:
            raise ValueError("Invalid worker instance")

    @property
    def workers(self):
        return self._workers


class Worker:
    def __init__(self, id_: int, name: str, company: str, boss: Boss):
        self.id = id_
        self.name = name
        self.company = company
        self._boss = None  
        self.boss = boss  

    @property
    def boss(self):
        return self._boss

    @boss.setter
    def boss(self, new_boss):
        if isinstance(new_boss, Boss):
            self._boss = new_boss
        else:
            raise ValueError("Invalid boss instance")


boss1 = Boss(1, "John", "ABC Company")
boss2 = Boss(2, "Alice", "XYZ Company")

worker1 = Worker(101, "Bob", "ABC Company", boss1)

print(worker1.boss.name)

worker2 = Worker(102, "Charlie", "XYZ Company", boss2)

try:
    worker2.boss = boss1
except ValueError as e:
    print(f"Error: {e}")

boss2.add_worker(worker2)

print([worker.name for worker in boss2.workers])
