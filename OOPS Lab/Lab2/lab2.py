#[1].
'''a=int(input("Enter a number : "))
b=int(input("Enter a number : "))
c=int(input("Enter a number : "))
if a>b:
    if a>c:
        print(a,"is the largest number.")
    else:
        print(c,"is the largest number.")
else:
    if b>c:
        print(b,"is the largest number.")
    else:
        print(c,"is the largest number.")
'''
#[2].
'''a=int(input("Enter a Year : "))
if a%4==0:
    print(a,"is a leap year.")
else:
    print(a,"is not a leap year.")
'''
#[3].
'''a=int(input("Enter 1 side of triangle : "))
b=int(input("Enter 2 side of triangle : "))
c=int(input("Enter 3 side of triangle : "))
if a+b<=c or b+c<=a:
    print("Triangle not possible")
elif a==b and b==c:
    print("It is an Equilateral Triangle.")
elif a==b or b==c or a==c:
    print("It is an Isosceles Triangle.")
else :
    print("It is a Scalene Triangle.")
'''
#[4].
'''a=int(input("Enter units consumed : "))
bill=sur=0
if a<0:
    print("Invalid Units.")
    exit()
elif a<=100:
    bill=5*a
elif a>100 and a<=200:
    bill=500+(a-100)*8
else :
    bill=1300+(a-200)*10
if bill>2000:
    sur=0.05*bill
print("Bill = $",bill+sur,sep='')
'''
#[5].
'''age = int(input("Enter age: "))
travel_class = input("Enter travel class (1st class, 2nd class, Sleeper): ").lower()
distance = float(input("Enter distance in km: "))

fare_per_km = 0
if travel_class == "1st class":
    fare_per_km = 5
elif travel_class == "2nd class":
    fare_per_km = 3
elif travel_class == "sleeper":
    fare_per_km = 2
else:
    print("Invalid travel class entered.")
    exit()

fare = fare_per_km * distance

if age < 12:
    fare *= 0.50
elif age > 60:
    fare *= 0.60

if distance > 500:
    fare *= 0.90

print("Total railway fare: Rs",fare,sep='')
'''
#[6].
'''balance=10000
amount = int(input("Enter withdrawal amount: "))

if amount % 100 != 0:
    print("Error: Amount should be multiple of 100")
elif amount > balance:
    print("Insufficient balance")
else:
    balance -= amount
    print("Transaction successful!")
    print("Remaining balance:", balance)
'''