#46 Default & Parameterized Constructors
class Student:
    def __init__(self, name="Unknown", age=0):   # default + parameterized
        self.name = name
        self.age = age

    def show(self):
        print(self.name, self.age)

s1 = Student()                 # default
s2 = Student("Mehak", 20)      # parameterized

s1.show()
s2.show()
