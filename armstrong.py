n=int(input("Enter a armstrong number:"))
tem=n
sum=0
while tem>0:
    r=tem%10
    sum=sum+r*r*r
    tem=tem//10
if n==sum:
    print("The nummber is armstrong")
else:
    print("The number is not armstrong")
