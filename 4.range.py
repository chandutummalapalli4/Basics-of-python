'''Classify:
0–50 → Low
51–100 → Medium
100 → High
negative → Invalid'''
num1=int(input("Enter a number"))
if 0<=num1<=50:
    print("Low")
elif 51<=num1<=100:
    print("Medium")
elif num1<0:
    print("invalid")
else:
    print("high")
