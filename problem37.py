#37. Multiple Inheritance
class Mother:
    def mother_info(self):
        print("This is mother")

class Father:
    def father_info(self):
        print("This is father")

class Child(Mother, Father):
    def child_info(self):
        print("This is child")

c = Child()
c.mother_info()
c.father_info()
c.child_info()
