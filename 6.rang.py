#Check if a number is within a given range (inclusive).
num = int(input("Enter the number: "))
low = int(input("Enter lower limit: "))
high = int(input("Enter upper limit: "))

if low <= num <= high:
    print("Number is in range")
else:
    print("Number is not in range")
