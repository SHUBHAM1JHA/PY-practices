def ma (a,b,c):
    if a>b and a>c:
        return (a)
    elif b>a and b>c:
        return (b)
    else:
        return (c)

sa=ma(1,2,3)
print ("grestest num is %d"%sa)
