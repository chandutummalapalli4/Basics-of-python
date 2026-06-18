## 3.problem
num1=int(input("Enter a Number:"))
if num1%3==0:
    print("Divisible by 3")
elif num1%5==0:
    print("Divisible by 5")
elif num1%3==0 and num1%5==0:
    print("Divisible by both 5 and 3")
else:
    print("Not divisible by both numbers")