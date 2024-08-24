class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def is_adult(self):
        return self.age >= 18

name = input("Enter your name: ")
age = int(input("Enter your age: "))
person = Person(name, age)
print(person.is_adult())

Person Class with is_adult Method