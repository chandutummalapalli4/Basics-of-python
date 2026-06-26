n=int(input("Enter a Value:"))
sum=0
product=1
while n>0:
    digits=n%10
    sum+=digits
    product*=digits
    n//=10
if product==sum:
    print("Spy Number")
else:
    print("Not a spy number")
