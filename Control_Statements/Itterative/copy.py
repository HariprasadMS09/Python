import time
saved_card_no = 1234
saved_pin = 5678
while(True):
    entered_card_no = int(input("Insert your card here\n"))
    if(entered_card_no != saved_card_no):
        print("Card cannot be read \n")
    else:
        for i in range(3):
            entered_pin = int(input("Enter your current pin \n"))
            if(entered_pin != saved_pin):
                print("Wrong pin try again")
                if(i==2):
                    for h in range(23, -1, -1):
                        for m in range(59, -1, -1):
                            for s in range(59, -1, -1):
                                print(h,":",m,":",s)
                                time.sleep(1)
            else:
                print("change pin?\nType 'Y' to change pin 'N' to exit")
                opinion = input()
                if(opinion == 'Y'):
                    saved_pin = int(input("Create new pin \n")) 
                    print("Congrats, Pin changed try transacting after some time \n")
                    for _ in range(3):
                        entered_pin = int(input("Enter your ATM pin: "))
                        if entered_pin != saved_pin:
                            print("Wrong pin. Try again.")
                            if (_ == 3):
                                for h in range(23, -1, -1):
                                    for m in range(59, -1, -1):
                                        for s in range(59, -1, -1):
                                            print(h,":",m,":",s)
                                            time.sleep(1)
                        else:
                            print("Your transaction is being processed.")
                            break
                else:
                    print("Thank you for banking with us \n")
                    break 
            if(entered_pin == saved_pin):
                break
    if(entered_card_no == saved_card_no):
        break  




