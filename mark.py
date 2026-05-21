m1=int(input("Enter m1:"))
m2=int(input("Enter m2:"))
m3=int(input("Enter m3:"))
m4=int(input("Enter m4:"))
m5=int(input("Enter m5:"))
print("m1=",m1)
print("m2=",m2)
print("m3=",m3)
print("m4=",m4)
print("m5=",m5)
total=m1+m2+m3+m4+m5
print("Total mark=",total)
if(m1>=50 and m2>=50 and m3>=50 and m4>=50 and m5>=50):
    print("PASS")
    print("Average mark:",total/5)
else:
    print("FAIL")
