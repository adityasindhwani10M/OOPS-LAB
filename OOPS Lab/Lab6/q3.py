def arms(a):
    t=a; s=0
    l=len(str(a))
    for i in range(l):
        s+=((t%10)**l)
        t//=10
    if s==a:
        print(a)

a,b=map(int,input("Enter the range with a space: ").split())
for i in range(a,b+1):
    arms(i)