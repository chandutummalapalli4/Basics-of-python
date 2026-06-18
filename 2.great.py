a, b, c = map(int, input("Enter the numbers: ").split())

largest = a

if b > largest:
    largest = b

if c > largest:
    largest = c

print(largest, "is greatest")