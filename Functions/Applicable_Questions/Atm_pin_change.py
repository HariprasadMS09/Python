import time
def change_pin():
    print("Forgot password ?\nType 'y' to change password 'n' to continue")
    opinion = input()
    if(opinion == "n"):
        Atm_login()
    else:
        global saved_pin
        saved_pin = int(input("Enter new password \n"))
        print("Password changed, try loging in again \n")
        Atm_login()
    
def Atm_login():    
    while(True):
        entered_card_no = int(input("Insert your card \n"))
        if(entered_card_no != saved_card_no):
            print("card cannot be read, try again\n")
        else:
            for i in range(1,4):
                entered_pin = int(input("Enter Atm pin \n"))
                if(entered_pin != saved_pin):
                    print("Wrong pin try again \n")
                    if (i==3):
                        change_pin()
                else:
                    print("Your transaction is being processed")
                    time.sleep(3)
                    print("Thank you for banking with us. ")
                    break
        if (entered_card_no == saved_card_no):
            break

saved_card_no = 1234
saved_pin = 5678

Atm_login()
