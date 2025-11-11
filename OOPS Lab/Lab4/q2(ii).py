'''
       1
     1 2 1
   1 2 3 2 1
 1 2 3 4 3 2 1
'''
n=int(input("Enter number of rows to print : "))
for i in range(1,n+1):
    print(" "*((n-i)*2),end='')
    for j in range(1,i+1):
        print(f"{j} ",end='')
    for j in range(i-1,0,-1):
        print(f"{j} ",end='')
    print()
