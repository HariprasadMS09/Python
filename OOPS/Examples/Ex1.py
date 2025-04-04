class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def get_make(self):
        return self.make
    
    def get_model(self):
        return self.model
    
    def get_year(self):
        return self.year
    
    def display_info(self):
        print(f"Car Information:")
        print(f"Make: {self.get_make()}")
        print(f"Model: {self.get_model()}")
        print(f"Year: {self.get_year()}")


car1 = Car("Toyota", "Camry", 2022)
car2 = Car("Ford", "Mustang", 2020)


car1.display_info()
print()
car2.display_info()