a,b,c=3,
if a>=b:       #or a>=c
    if a>b and a>c:
        print(a)
    elif a==b and b>c:
        print(a,b)
    elif a==c and c>b:
        print(a,c)
    elif a==b and a==c:
        print(a,b,c)
    elif c>a:
        print(c)
elif (b>=c):
    if(b>c):
        print(b)
    elif(b==a):
        print(b,a)
    elif(b==c):
        print(b,c)
else:
    if((c>a) and (c>b)):
        print(c)