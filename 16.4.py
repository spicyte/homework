class CustomException(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.log_message(message)

    def log_message(self, message):
        try:
            with open('logs.txt', 'a') as log_file:
                log_file.write(f"Error: {message}\n")
        except Exception as e:
            print(f"Failed to log the error message: {e}")

try:
    raise CustomException("Something went wrong!")
except CustomException as ce:
    print(f"Caught CustomException: {ce}")
