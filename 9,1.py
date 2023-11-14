from project import greet

def main():
    user_name = input("Введiть ваше iм`я: ")
    greeting_message = greet(user_name)
    print(greeting_message)

if __name__ == "__main__":
    main()
