from node import Node

class Stack:
    def __init__(self):
        self._top = None
        self._size = 0

    def is_empty(self):
        return self._top is None

    def size(self):
        return self._size

    def push(self, item):
        new_node = Node(item)
        new_node.set_next(self._top)
        self._top = new_node
        self._size += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        popped_item = self._top.get_data()
        self._top = self._top.get_next()
        self._size -= 1
        return popped_item

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self._top.get_data()

    def __repr__(self):
        representation = "<Stack: "
        current = self._top
        while current is not None:
            representation += f"{current.get_data()} "
            current = current.get_next()
        return representation + ">"

if __name__ == "__main__":
    stack = Stack()

    stack.push(1)
    stack.push(2)
    stack.push(3)

    print("Stack:", stack)
    print("Size:", stack.size())
    print("Peek:", stack.peek())

    popped_item = stack.pop()
    print("Popped Item:", popped_item)
    print("Stack after pop:", stack)
    print("Size after pop:", stack.size())
