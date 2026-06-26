n = int(input("Enter a value of N: "))

reverse=0
while n > 0:
    digit = n % 10
    
    if digit % 2 == 0:
        found = True
        reverse=reverse*10+digit
    
    n //= 10
print("Reverse of even numbers:",reverse)
