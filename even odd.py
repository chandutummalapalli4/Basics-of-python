'''Even / Odd / Zero
Write a program to check:
If number is 0 → print "Zero"
If number is even → print "Even"
Else → print "Odd" '''

num =int(input("Enter the Number :"))
if num==0:
    print("Zero")
elif num%2==0:
    print("Even")
else:
    print("Odd")