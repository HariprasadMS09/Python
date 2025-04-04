t = (1,2,3,4,5)
t1 = list(t)
t2 = [6,7,8,9,10]
t1.extend(t2)
t = tuple(t1)
print(t)
print(type(t))