
#   F = C × 1.8 + 32

def f(x):
    fa = x * 1.8 + 32
    return fa

c= int(input("Enter temperature in ^c : \n\t==> "))
F=f(c)
print (c,"^c in farhenheit scale is",F,"^f")
