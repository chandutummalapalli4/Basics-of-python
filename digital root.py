n = int(input("Enter a value: "))

while n >= 10:          # repeat until single digit
    total = 0
    
    while n > 0:       # find sum of digits
        digit = n % 10
        total += digit
        n //= 10
    
    n = total          # replace n with new sum

print("Digital Root:", n)