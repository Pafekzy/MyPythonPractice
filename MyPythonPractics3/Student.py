class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average_grade(self):
        return sum(self.grades) / len(self.grades)

    def display(self):
        print(f"Student Name: {self.name}")
        print(f"Average Grade: {self.average_grade()}")

name = input("Enter student's name: ")
grades = list(map(int, input("Enter grades separated by spaces: ").split()))
student = Student(name, grades)
student.display()


