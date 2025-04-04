def Add(*a):
    length = len(a)
    sum = 0
    for i in range(length):
        sum = sum + a[i]
    print("Sum = ", sum)

def Sub(*a):
    length = len(a)
    diff = a[0]
    for i in range(1,length):
        diff = diff - a[i]
    print("Diffrence = ", diff) 
    
def Multiply(*a):
    length = len(a)
    pro = 1
    for i in range(length):
        pro = pro * a[i]
    print("Product = ", pro)
    
def Divide(*a):
    length = len(a)
    quo = a[0]
    for i in range(1,length):
        if(a[i] == 0):
            print("Error:Divide by zero")
            break
        else:
            quo = quo / a[i]
    print("Quotient = ", quo)
    

    
Divide(30,5)