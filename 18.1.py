import re

class EmailValidator:
    def __init__(self, email):
        self.validate(email)
        self.email = email

    @classmethod
    def validate(cls, email):
        email_pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
        if not re.match(email_pattern, email):
            raise ValueError("Invalid email address")

try:
    valid_email_instance = EmailValidator('example@email.com')
    print("Valid email:", valid_email_instance.email)

    invalid_email_instance = EmailValidator('invalid_email')
except ValueError as e:
    print(f"Error: {e}")



