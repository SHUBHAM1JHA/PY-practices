n = int (input ("enter the number ::: "))
for i in range (2,101):
    if n==i:
        continue

    if (n%i)==0:
        print('its not a prime number')
        break
    else:
        print("its a prime number")
        break
