#Single Inheritance
class Animal:      # Parent class
    def sound(self):
        print("Animals make sounds")

class Dog(Animal):  # Child class
    def bark(self):
        print("Dog barks")

d = Dog()
d.sound()
d.bark()
