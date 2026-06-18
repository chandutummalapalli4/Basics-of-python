char=int(input("Enter input"))
if 0<=char<=50 :
    print("Low")
elif 51<=char<=100:
    print("Medium")
elif char<0:
    print("invalid")
else:
    print("high")
