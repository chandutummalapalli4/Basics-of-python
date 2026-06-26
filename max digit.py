n=int(input("Enter a Nuimber:"))
max_digit=5
while n>0:
    digit=n%10
    n//=10
if digit==max_digit:
    print("yes")
else:
    print("No")