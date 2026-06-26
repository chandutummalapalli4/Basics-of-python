n = int(input("Enter a Number: "))

found3 = False
found7 = False

while n > 0:
    digit = n % 10
    
    if digit == 3:
        found3 = True
    if digit == 7:
        found7 = True
    
    n //= 10

if found3 and found7:
    print("Yes")
else:
    print("No")