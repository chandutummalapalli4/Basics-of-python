n=int(input("Enter a Number:"))
total=0
reverse=0
count=0
while n>0:
    digit=n%10
    total+=digit
    count+=1
    reverse=reverse*10+digit
    n//=10
print("Reverse of Number:",reverse)
print("Sum of Digits:",total)
print("Count of Digits:",count)