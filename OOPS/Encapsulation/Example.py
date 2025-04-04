class Operation:
    def Addition(cls,x,y):
        z = x + y
        print("Sum = ", z)

    def Multiply(cls,x,y):
        z = x * y
        print("Product = ",z)

obj = Operation()
obj.Addition(3,6)
obj.Multiply(5,7)