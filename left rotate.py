n = int(input("Enter a Number: "))
k = int(input("Enter k rotations: "))

# Step 1: Count digits
count = 0
temp = n
while temp > 0:
    count += 1
    temp //= 10

# Step 2: Reduce k
k = k % count

# Step 3: Find divisor
divisor = 10 ** (count - 1)

# Step 4: Perform k left rotations
for _ in range(k):
    first_digit = n // divisor
    remaining = n % divisor
    n = (remaining * 10) + first_digit

# Step 5: Output
print("Left Rotated Number:", n)