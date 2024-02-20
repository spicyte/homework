from node import Node

class Queue:
    def __init__(self):
        self._front = None
        self._rear = None
        self._size = 0

    def is_empty(self):
        return self._size == 0

    def size(self):
        return self._size

    def enqueue(self, item):
        new_node = Node(item)
        if self.is_empty():
            self._front = new_node
        else:
            self._rear.set_next(new_node)
        self._rear = new_node
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        item_to_remove = self._front.get_data()
        self._front = self._front.get_next()
        if self._front is None:
            self._rear = None
        self._size -= 1
        return item_to_remove

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty queue")
        return self._front.get_data()

    def __repr__(self):
        representation = "<Queue: "
        current = self._front
        while current is not None:
            representation += f"{current.get_data()} "
            current = current.get_next()
        return representation + ">"

if __name__ == "__main__":
    queue = Queue()

    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    print("Queue:", queue)
    print("Size:", queue.size())
    print("Peek:", queue.peek())

    dequeued_item = queue.dequeue()
    print("Dequeued Item:", dequeued_item)
    print("Queue after dequeue:", queue)
    print("Size after dequeue:", queue.size())
