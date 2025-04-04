import time
saved_pin = 1234
for _ in range(3):
    entered_pin = int(input("Enter your ATM pin: "))
    if entered_pin != saved_pin:
        print("Wrong pin. Try again.")
    else:
        print("Your transaction is being processed.")
        break
else:
        for h in range(23, -1, -1):
            for m in range(59, -1, -1):
                for s in range(59, -1, -1):
                    print(h,":",m,":",s)
                    time.sleep(1)
                    

