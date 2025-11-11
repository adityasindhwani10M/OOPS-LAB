'''
1
2   3
4   5   6
7   8   9   10
'''
a=1
row=int(input("Enter number of rows to be printed : "))
for i in range (row):
    for j in range(0,i+1):
        print(a,end='\t')
        a+=1
    print()
