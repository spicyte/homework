class FileContextManager:
    def __init__(self, filename, mode='r'):
        self.filename = filename
        self.mode = mode
        self.file = None
        self.counter = 0

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        self.counter += 1
        print(f"File '{self.filename}' opened. Counter: {self.counter}")
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        self.counter -= 1
        self.file.close()
        print(f"File '{self.filename}' closed. Counter: {self.counter}")


        if exc_type is not None:
            print(f"Exception Type: {exc_type}")
            print(f"Exception Value: {exc_value}")
            print(f"Traceback: {traceback}")


        return False


with FileContextManager('example.txt', 'w') as file:
    file.write("Hello, World!")
