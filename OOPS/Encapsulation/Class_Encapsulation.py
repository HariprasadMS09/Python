class my_class:
    log_in = "08:30"
    Snack_break = "11:00"
    Lunch = "13:30"
    Tea_break = "15:00"
    log_out = "20:30"
    def Show_Timings(cls):
        print("Log in = ", cls.log_in)
        print("Snack break = ", cls.Snack_break)
        print("Lunch = ", cls.Lunch)
        print("Tea break = ", cls.Tea_break)
        print("Log out = ", cls.log_out)

obj = my_class()
obj.Show_Timings()
    