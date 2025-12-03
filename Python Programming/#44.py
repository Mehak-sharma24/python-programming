# 44 Student class with methods
class Student:
    def __init__(self, name):
        self.name = name

    def show(self):
        print("Student Name:", self.name)

s = Student("Mehak")
s.show()
