n = int(input("Enter a value: "))

count = 0
fou_digit=7
while n > 0:
    digit = n % 10
    
    if digit == fou_digit:
        count += 1
    
    n //= 10

print("Count of 7:", count)