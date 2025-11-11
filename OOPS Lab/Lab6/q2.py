def strong(a):
    t=a; sum=0
    while t>0:
        fact=1
        for i in range(1,t%10+1): fact*=i;
        sum+=fact
        t//=10
    print("It is a Strong number" if a==sum else "It is not a Strong number")
num=int(input("Enter a number: "))
strong(num)