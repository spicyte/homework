class Dog:
    age_factor = 7
    def __init__(self, dog_age):
        self.dog_age = dog_age

    def human_age(self):
        equivalent_age = self.dog_age * self.age_factor
        return equivalent_age

dog1 = Dog(3)
print(f"The dog is {dog1.dog_age} years old in dog years.")
print(f"In human years, the dog is approximately {dog1.human_age()} years old.")

