# Constructor Overloading in Python (Simulated)
class Student:
    def __init__(self, name="Unknown", age=0):   # one constructor with defaults
        self.name = name
        self.age = age

    def show(self):
        print("Name:", self.name)
        print("Age:", self.age)

# Different ways of calling the same constructor
s1 = Student()
s2 = Student("Mehak")
s3 = Student("Mehak", 20)

s1.show()
s2.show()
s3.show()
