print("enter the choice")
print("press the number 1=add")
print("press the number 2=sub")
print("press the number 3=mul")
print("press the number 4=div")
print("press the number 5=module")
ch=int(input("Enter the choice "))
if ch==1:
    a=int(input("enter the first number"))
    b=int(input("enter the second number"))
    print(a+b)
elif ch==2:
    a=int(input("enter the first number"))
    b=int(input("enter the second number"))
    print(a-b)
elif ch==3:
    a=int(input("enter the first number"))
    b=int(input("enter the second number"))
    print(a*b)
elif ch==4:
    a=int(input("enter the first number"))
    b=int(input("enter the second number"))
    print(a/b)
else:#else does not condetion
    a=int(input("enter the first number"))
    b=int(input("enter the second number"))
    print(a%b)
