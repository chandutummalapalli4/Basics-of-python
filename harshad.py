n=int(input("Enter a value:"))
total=0
while n>0:
    digits=n%10
    total+=digits
    n//=10
print("Sum:",total)
if n%total==0:
    print("Harshad Number")
else:
    print("Not")    