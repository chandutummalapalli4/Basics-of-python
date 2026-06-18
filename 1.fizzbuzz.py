'''Divisible Logic (Advanced)
Print:
"FizzBuzz" → divisible by both 3 & 5
"Fizz" → only 3
"Buzz" → only 5
"None" → otherwise'''
num1=int(input("Enter a Number :"))
if num1%3==0 and num1%5==0:
    print("Divisible by both 3 and 5")
elif num1%3==0:
    print("Divisible by 3")
elif num1%5==0:
    print("Divisible by 5")
else:
    print("Not divisible by both")