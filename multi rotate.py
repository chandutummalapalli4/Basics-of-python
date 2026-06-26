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

# Step 3: Perform rotation k times
for _ in range(k):
    last_digit = n % 10
    remaining = n // 10
    n = (last_digit * (10 ** (count - 1))) + remaining

# Step 4: Output
print("Rotated Number:", n)