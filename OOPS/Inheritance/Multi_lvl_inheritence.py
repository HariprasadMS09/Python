class Grand_parent:
    Land = "4 Acer"
    def Grand_parent_networth(self):
        print("Grand parent networth:")
        print("Land = ",self.Land)
        print()

class Parent(Grand_parent):
    Site = 5
    Amt = 500000
    def Parent_networth(self):
        print("Parent networth:")
        print("Land = ",self.Land)
        print("Site = ",self.Site)
        print("Amt = ",self.Amt)
        print()

class child(Parent):
    crypto = 20000000
    def child_net_worth(self):
        print("Child networth:")
        print("Land = ",self.Land)
        print("Site = ",self.Site)
        print("Amt = ",self.Amt)
        print("crypto = ",self.crypto)


obj = child()
obj.Grand_parent_networth()
obj.Parent_networth()
obj.child_net_worth()
