
def det(x):
    u=0
    l=0
    for i in x:

        if (i.isupper())== True:
            u=u+1
        elif (i.islower())== True:
            l=l+1
        else:
            pass
    return (u,l)

str= "The quick Brow Fox"
a,b= det(str)
print ("No. of upper case characters : " , a)
print ("No. of lower case characters : " , b)
