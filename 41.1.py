class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)


def reverse_input():
    s = Stack()
    sequence = input("Символ: ")

    for char in sequence:
        s.push(char)

    reversed_sequence = ""

    while not s.is_empty():
        reversed_sequence += s.pop()

    print("Послiдовнiсть:", reversed_sequence)


if __name__ == "__main__":
    reverse_input()
