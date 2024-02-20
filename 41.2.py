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


def is_balanced(expression):
    stack = Stack()
    opening_brackets = "({["
    closing_brackets = ")}]"
    brackets_map = {")": "(", "}": "{", "]": "["}

    for char in expression:
        if char in opening_brackets:
            stack.push(char)
        elif char in closing_brackets:
            if stack.is_empty():
                return False
            elif stack.peek() == brackets_map[char]:
                stack.pop()
            else:
                return False

    return stack.is_empty()


if __name__ == "__main__":
    sequence = input("введiть символ: ")
    if is_balanced(sequence):
        print("Скобки сбалансованi.")
    else:
        print("Скобки не сбалансированi.")
