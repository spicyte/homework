class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

    def size(self):
        return len(self.items)

    def get_from_stack(self, e):
        found = False
        temp_stack = Stack()
        
        while not self.is_empty():
            item = self.pop()
            if item == e:
                found = True
                break
            else:
                temp_stack.push(item)

        while not temp_stack.is_empty():
            self.push(temp_stack.pop())

        if found:
            return e
        else:
            raise ValueError(f"Елемент {e} не найден в стеке.")

if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)

    try:
        element = stack.get_from_stack(3)
        print(f"Знайден елемент: {element}")
    except ValueError as e:
        print(e)

    try:
        element = stack.get_from_stack(5)
        print(f"Знайден елемент: {element}")
    except ValueError as e:
        print(e)
