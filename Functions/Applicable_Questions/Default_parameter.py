def Accounting(Financial_year, Book_begining_date=None):
    # If Book_begining_date is not provided, initialize it to Financial_year
    if Book_begining_date is None:
        Book_begining_date = Financial_year
        
    print("Financial year date=", Financial_year)
    print("Book beginning date =", Book_begining_date)

fi_year = input("Enter the current Financial year \n")
Bk_date = input("Enter book beginning date (leave blank to use financial year) \n") or None
Accounting(fi_year, Bk_date)
