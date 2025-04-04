class Parent:
    Land = 4 
    Site = 6
    Amt = 500000

class Child1(Parent):
    crypto = 10000000
    def child1_net_worth(self):
        print("Child 1 networth:")
        print("Land = ",0.5*self.Land, " Acre")
        print("Site = ",0.5*self.Site)
        print("Amt = ",0.5*self.Amt)
        print("crypto = ",self.crypto)
    
class Child2(Parent):
    job = "50LPA"
    def child2_net_worth(self):
        print("Child 2 networth:")
        print("Land = ",0.5*self.Land, " Acre")
        print("Site = ",0.5*self.Site)
        print("Amt = ",0.5*self.Amt)
        print("job = ",self.job)

obj1 = Child1()
obj2 = Child2()
obj1.child1_net_worth()
obj2.child2_net_worth()