import json
import os

class PhoneBook:
    def __init__(self, filename):
        self.filename = filename
        self.contacts = self.load_data()

    def load_data(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                data = json.load(file)
                return data.get('contacts', [])
        else:
            print(f"Файл {self.filename} не знайден. Створена нова телефона книга.")
            return []

    def save_data(self):
        data = {'contacts': self.contacts}
        with open(self.filename, 'w') as file:
            json.dump(data, file, indent=2)

    def add_contact(self, contact):
        self.contacts.append(contact)
        print(f"Контакт {contact} додан.")

    def search_contacts(self, key, value):
        results = [contact for contact in self.contacts if value.lower() in str(contact[key]).lower()]
        print_results(results)

    def remove_contact(self, phone_number):
        self.contacts = [contact for contact in self.contacts if str(contact['phone']) != str(phone_number)]
        print(f"Контакт с номером телефона {phone_number} видален.")

    def update_contact(self, phone_number, new_contact):
        for i, contact in enumerate(self.contacts):
            if str(contact['phone']) == str(phone_number):
                self.contacts[i] = new_contact
                print(f"Контакт с номером телефона {phone_number} оновлен.")
                return
        print(f"Контакт с номером телефона {phone_number} не знайден.")

    def exit_program(self):
        self.save_data()
        print("Данi сбереженi.")
        exit()


def print_results(results):
    if not results:
        print("Не знайдено.")
    else:
        for contact in results:
            print(contact)


def main():
    phone_book_filename = input("Введиiть iм я файла (наприклад, phone_book.json): ")
    phone_book = PhoneBook(phone_book_filename)

    while True:
        print("\nОберiть дiю:")
        print("1. Додати новий контакт")
        print("2. Пошук за iм ям")
        print("3. Пошук по призвищу")
        print("4. Пошук по номеру телефона")
        print("5. Видалити контакт по номеру телефона")
        print("6. Оновити контакт по номеру телефона")
        print("7. Вийти из программы")

        choice = input("Введить номер: ")

        if choice == '1':
            contact = {'name': input("Iмя: "),
                       'surname': input("Прiзвище: "),
                       'phone': input("номер телефона: "),
                       'location': input("город або штат: ")}
            phone_book.add_contact(contact)

        elif choice in ('2', '3', '4'):
            key = { '2': 'name', '3': 'surname', '4': 'phone' }[choice]
            value = input(f"Ведiть {key} для пошука: ")
            phone_book.search_contacts(key, value)

        elif choice == '5':
            phone_number = input("Введить номер телефона для видалення: ")
            phone_book.remove_contact(phone_number)

        elif choice == '6':
            phone_number = input("Введiть номер телефона для оновлення: ")
            new_contact = {'name': input("Введiть нове iмя: "),
                           'surname': input("Введiть нове прiзвище: "),
                           'phone': input("Введiть новий номер телефона: "),
                           'location': input("Введiть новий город или штат: ")}
            phone_book.update_contact(phone_number, new_contact)

        elif choice == '7':
            phone_book.exit_program()

        else:
            print("Оберiть, вiд 1 до 7.")


if __name__ == "__main__":
    main()
