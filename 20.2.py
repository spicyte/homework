import unittest

class PhoneBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone):
        self.contacts[name] = {"phone": phone}

    def get_contact_by_name(self, name):
        return self.contacts.get(name)

class TestPhoneBook(unittest.TestCase):

    def setUp(self):
        self.phonebook = PhoneBook()

    def test_add_contact(self):
        contact_name = "Kate"
        contact_phone = "123-456-7890"
        self.phonebook.add_contact(contact_name, contact_phone)

        added_contact = self.phonebook.get_contact_by_name(contact_name)
        self.assertIsNotNone(added_contact)
        self.assertEqual(added_contact["phone"], contact_phone)

if __name__ == '__main__':
    unittest.main()
