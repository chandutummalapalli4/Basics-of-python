n=int(input("Enter n Value:"))
digit_found=5
count=0
while n>0:
    digit=n%10
    if digit>digit_found:
        count+=1
    n//=10
print("Count:",count)