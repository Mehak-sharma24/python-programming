#38. Method Overloading (Simulated)
class Math:
    def add(self, a=0, b=0, c=0):
        print("Sum =", a + b + c)

m = Math()
m.add(5)
m.add(5, 10)
m.add(5, 10, 15)
