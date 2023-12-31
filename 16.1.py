class Person:
    def method(self, name, salary):
        return name + str(salary)

class Student(Person):
    def method(self, name, salary=None):
        c = super().method(name, salary)
        print("student method")
        return c


student_instance = Student()
print(student_instance.method(name="Kate"))

class Teacher(Person):
    def method(self, name, salary):
        a = super().method(name, salary)
        print("teacher method")
        return a

teacher_instance = Teacher()
print(teacher_instance.method(name="Anna", salary=8000))

