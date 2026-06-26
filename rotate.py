n = int(input("Enter a Number: "))

# Step 1: Extract last digit
last_digit = n % 10

# Step 2: Remove last digit
remaining = n // 10

# Step 3: Count digits of remaining
count = 0
temp = remaining

while temp > 0:
    count += 1
    temp //= 10

# Step 4: Build rotated number
result = (last_digit * (10 ** count)) + remaining

# Step 5: Output
print("Rotated Number:", result)