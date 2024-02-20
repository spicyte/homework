from node import Node

class UnsortedList:

    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head is None

    def add(self, item):
        temp = Node(item)
        temp.set_next(self._head)
        self._head = temp

    def size(self):
        current = self._head
        count = 0
        while current is not None:
            count += 1
            current = current.get_next()

        return count

    def search(self, item):
        current = self._head
        found = False
        while current is not None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()

        return found

    def remove(self, item):
        current = self._head
        previous = None
        found = False
        while not found and current is not None:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()

        if found:
            if previous is None:
                self._head = current.get_next()
            else:
                previous.set_next(current.get_next())

    def index(self, item):
        current = self._head
        index = 0
        while current is not None:
            if current.get_data() == item:
                return index
            current = current.get_next()
            index += 1
        raise ValueError(f"{item} is not in list")

    def insert(self, pos, item):
        if pos <= 0:
            self.add(item)
        elif pos >= self.size():
            self.append(item)
        else:
            current = self._head
            for _ in range(pos - 1):
                current = current.get_next()
            temp = Node(item)
            temp.set_next(current.get_next())
            current.set_next(temp)

    def pop(self, pos=None):
        if pos is None:
            pos = self.size() - 1
        if pos < 0 or pos >= self.size():
            raise IndexError("pop index out of range")
        current = self._head
        if pos == 0:
            self._head = current.get_next()
            return current.get_data()
        for _ in range(pos - 1):
            current = current.get_next()
        popped_item = current.get_next().get_data()
        current.set_next(current.get_next().get_next())
        return popped_item

    def slice(self, start, stop):
        if start < 0:
            start = 0
        if stop > self.size():
            stop = self.size()
        if start >= stop:
            return UnsortedList()
        current = self._head
        for _ in range(start):
            current = current.get_next()
        sliced_list = UnsortedList()
        while current is not None and start < stop:
            sliced_list.append(current.get_data())
            current = current.get_next()
            start += 1
        return sliced_list

    def __repr__(self):
        representation = "<UnsortedList: "
        current = self._head
        while current is not None:
            representation += f"{current.get_data()} "
            current = current.get_next()
        return representation + ">"

if __name__ == "__main__":
    my_list = UnsortedList()

    my_list.add(31)
    my_list.add(77)
    my_list.add(17)
    my_list.add(93)
    my_list.add(26)
    my_list.add(54)

    print(my_list.size())
    print(my_list)
    print(my_list.search(93))
    print(my_list.search(100))

    my_list.add(100)
    print(my_list.search(100))
    print(my_list.size())

    my_list.remove(54)
    print(my_list.size())
    my_list.remove(93)
    print(my_list.size())
    my_list.remove(31)
    print(my_list.size())
    print(my_list.search(93))

    print(my_list.index(17))
    my_list.insert(2, 99)
    print(my_list)
    print(my_list.pop())
    print(my_list)

    sliced_list = my_list.slice(1, 4)
    print(sliced_list)
