n = int(input("Enter a number: "))

original = n

# Step 1: Count digits
count = 0
temp = n

while temp > 0:
    count += 1
    temp //= 10

# Step 2: Calculate Armstrong sum
temp = n
armstrong_sum = 0

while temp > 0:
    digit = temp % 10
    armstrong_sum += digit ** count
    temp //= 10

# Step 3: Compare
if armstrong_sum == original:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")