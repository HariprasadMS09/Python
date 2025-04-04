class Job:
    Year_of_Exp = 2
    __Salary = 30000 #private Attribute
    def Show_Timings(cls):
        print("Year of Exp = ",cls.Year_of_Exp)
        #print("Salary = ", Salary) #Error: Name Salary is not defined

obj = Job()
print("Year of Exp = ",obj.Year_of_Exp)
print("Salary = ",obj._Job__Salary) #Name mangling method
    