n = int(input("Enter a number: "))

count = 0

while n > 0:
    n = n // 10
    count += 1
    sum+=count

print("Number of digits:", count)
print("sum of digits:",sum)