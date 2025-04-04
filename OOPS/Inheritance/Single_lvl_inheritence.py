class Parent:
    a = int(input("Enter a value \n"))
    b = int(input("Enter b value \n"))

class Child(Parent):
    obj1 = Parent()
    c = obj1.a + obj1.b
    def Result(self):
        print("Sum = ", self.c)

obj2 = Child()
obj2.Result()

