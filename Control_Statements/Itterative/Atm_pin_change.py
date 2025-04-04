import time
saved_card_no = 1234
saved_pin = 5678
while(True):
    entered_card_no=int(input("Insert your card \n"))
    if(entered_card_no != saved_card_no):
        print("Card cannot be read \n")
    else:
        opinion=input("Change password?\nType 'Y' to change password 'N' to get other options \n")
        if(opinion != "Y"):
            for i in range(3):
                entered_pin = int(input("Enter your pin \n"))
                if(entered_pin != saved_pin):
                    print("Wrong pin, Try again")
                    if(i==2):
                        for h in range(23, -1, -1):
                            for m in range(59, -1, -1):
                                for s in range(59, -1, -1):
                                    print(h,":",m,":",s)
                                    time.sleep(1)
                else:
                    print("Transaction sucessful\nThank you for banking with us \n")
                    break
        else:
            for i in range(3):
                entered_pin = int(input("Enter your current pin \n"))
                if(entered_pin != saved_pin):
                    print("Wrong pin, Try again")
                    if(i==2):
                        for h in range(23, -1, -1):
                            for m in range(59, -1, -1):
                                for s in range(59, -1, -1):
                                    print(h,":",m,":",s)
                                    time.sleep(1)
                else:
                     saved_pin = int(input("Create new pin \n"))
                     print("Congrates, pin changed\n Try transacting after some time \n")
                     break