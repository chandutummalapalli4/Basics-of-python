n=int(input("Enter a Number:"))
if n==0:
    pro=0
else:
    pro=1
while n>0:
    digit=n%10
    pro=pro*digit
    n//=10
print("Product of Digits:",pro)

## small among the digits
n=int(input("Enter a Nuimber:"))
small=9
while n>0:
    digit=n%10
    if digit<small:
        small=digit
    n//=10
print("smallest of digits:",small)