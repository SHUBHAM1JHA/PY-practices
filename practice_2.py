m1 = int(input("enter marks in english : "))
m2 = int(input("enter marks in maths : "))
m3 = int(input("enter marks in science : "))

tm = m1 + m2 + m3
p= tm/3

if m1<33 or m2<33 or m3<33:
    print (" you are failed ")
elif p<40: 
    print (" you are failed ")
else:
    print (" you are passed")

