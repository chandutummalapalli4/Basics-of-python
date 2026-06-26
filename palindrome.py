n=int(input("Enter n value:"))
reverse=0
n1=n
while n>0:
    digit=n%10
    reverse=reverse*10+digit
    n//=10
if reverse==n1:
    print("Palindrome")
else:
    print("Not a Plaindrome")