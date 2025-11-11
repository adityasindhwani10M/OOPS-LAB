'''
    *
  * * *
* * * * *
  * * *
    *
'''
n=int(input("Enter number(odd) of rows to print : "))
for i in range(1,n+1,2):
    print(" "*(n-i),end='')
    print("* "*i)
for j in range(n-2,0,-2):
    print(" "*(n-j),end='')
    print("* "*j)