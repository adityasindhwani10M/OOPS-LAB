def largePal(beg,end):
    for i in range(end, beg-1, -1):
        if i==int(str(i)[::-1]):
            print("Largest Palindrome =",i)
            break

a,b=map(int,input("Enter the range with a space: ").split())
print(a,b)
largePal(a,b)