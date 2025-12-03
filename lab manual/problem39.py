#39. Method Overriding
class Parent:
    def show(self):
        print("This is parent class")

class Child(Parent):
    def show(self):      # overriding
        print("This is child class")

c = Child()
c.show()
