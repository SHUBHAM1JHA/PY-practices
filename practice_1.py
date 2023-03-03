a= int (input("enter 1st  num \n\t"))
b= int (input("enter 2nd  num \n\t"))
c= int (input("enter 3rd  num \n\t"))
d= int (input("enter 4th  num \n\t"))

if a>b and a>c and a>d:
    print ("%d is greater"%a)
elif b>a and b>c and b>d:
    print ("%d is greater"%b)
elif c>a and c>b and c>d:
    print ("%d is greater"%c)
elif d>a and d>b and d>c:
    print ("%d is greater"%d)