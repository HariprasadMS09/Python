def change_pin():
    print("Forgot password ?\nType 'y' to change password 'n' to continue")
    opinion = input()
    if(opinion == "n"):
        gmail_login()
    else:
        global saved_pin
        saved_pin = input("Enter new password \n")
        print("Password changed, try loging in again \n")
        gmail_login()
    
def gmail_login():    
    while(True):
        entered_gmail = input("Enter your gmail \n")
        if(entered_gmail != saved_gmail):
            print("Gmail not found, enter correct Gmail \n")
        else:
            for i in range(1,6):
                entered_pin = input("Enter Gmail password \n")
                if(entered_pin != saved_pin):
                    print("Wrong pin try again \n")
                    if (i==5):
                        change_pin()
                else:
                    print("You are logged in ")
                    break
        if (entered_gmail == saved_gmail):
            break

saved_gmail = "hariprasadms01@gmail.com"
saved_pin = "1234"
gmail_login()
