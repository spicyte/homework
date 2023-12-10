class Animal:
    def __init__(self, talk):
        self.my_list = [talk]

class Dog(Animal):
    def __init__(self, talk):
        super().__init__(talk)

    def __str__(self) -> str:
        
        return f"{self.my_list[0]}"


user_input = input("Enter the talk attribute for the Dog: ")


dog_instance = Dog(talk=user_input)


print(dog_instance)

class Cat(Animal):
    def __init__(self, talk):
        super().__init__(talk)

    def __str__(self) -> str:
        return f"{self.my_list[0]}"

user_input = input("Enter the talk attribute for the Cat: ")


cat_instance = Cat(talk=user_input)

print(cat_instance)
