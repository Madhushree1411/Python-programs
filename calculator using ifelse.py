a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
print("1.add")
print("2.sub")
print("3.mul")
print("4.div")
choice=int(input("Enter choice:"))
if choice==1:
    print("Add=",a+b)
elif choice==2:
    print("Sub=",a-b)
elif choice==3:
    print("Mul=",a*b)
elif choice==4:
    print("Div=",a/b)
else:
    print("Invalid choice")
    
