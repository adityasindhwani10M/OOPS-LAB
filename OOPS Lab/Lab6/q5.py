n=int(input("Enter a number : "))
if n%sum(map(int, str(n)))==0:
    print("Niven Number")
else:
    print("Not a Niven Number")
