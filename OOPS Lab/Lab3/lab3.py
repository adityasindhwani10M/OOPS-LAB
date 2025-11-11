#[1].
'''
sub1=int(input("Enter marks of subject 1 : "))
sub2=int(input("Enter marks of subject 2 : "))
sub3=int(input("Enter marks of subject 3 : "))
sub4=int(input("Enter marks of subject 4 : "))
sub5=int(input("Enter marks of subject 5 : "))
avg=(sub1+sub2+sub3+sub4+sub5)/5.0
print(f"Average = {avg}")
if avg>=85 :
    print("Outstanding!")
elif avg>=75 and avg<85 :
    print("Excellent!")
elif avg>=65 and avg<75 :
    print("Very Good!")
elif avg>=60 and avg<65 :
    print("Good!")
elif avg>=50 and avg<60 :
    print("Average!")
elif avg>=35 and avg<50 :
    print("Need Hardwork!")
else :
    print("Poor Performance!")
'''
#[2].
'''for i in range(1,11,2):
    print(i)
'''
#[3].
'''n=int(input("Enter a number to reverse : "))
t=abs(n)
rev=0
sign=1
if n<0: sign=-1
while t!=0:
    rev=rev*10+t%10
    t//=10
print(f"Reverse of {n} is {rev*sign}.")
'''
#[4].
'''n=abs(int(input("Enter a number : ")))
t=n
sum=0
while t!=0:
    sum+=t%10
    t//=10
print(f"Sum of digits of {n} is {sum}.")
'''
#[5].
'''n=int(input("Enter a number : "))
t=abs(n)
rev=0
sign=1
if n<0: sign=-1
while t!=0:
    rev=rev*10+t%10
    t//=10
rev*=sign
if n==rev:
    print("It's a Palindrome number.")
else :
    print("Not Palindrome.")
'''
#[6].
'''num = int(input("Enter a number: "))
num_str = str(num)
n = len(num_str)
sum = 0
for digit in num_str:
    sum += int(digit) ** n
if sum == num:
    print("It is an Armstrong number.")
else:
    print("It is not an Armstrong number.")
'''