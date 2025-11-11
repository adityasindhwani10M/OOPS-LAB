a=int(input("Enter a number :"))
b=int(input("Enter a number :"))
ch=int(input("Press 1 to add these numbers, Press 2 to subrtract them, Press 3 to multiply, Press 4 to Divide first from second : "))
match(ch):
    case 1: print(a+b)
    case 2: print(a-b)
    case 3: print(a*b)
    case 4: print(a/b)
    case _: print("Wrong input.")