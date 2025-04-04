class parent():
    parent_age = 42
    wealth="38L"

    def show1(self):
        print(self.wealth)

class child(parent):
    def show2(self):
        print("Child details are ....")
        child_age=15
        print("Age = ",child_age)
        print("Child's parent age = ",self.parent_age)
        print("Child's parent wealth = ",self.wealth)
        
obj1 = child()
obj1.show2()
