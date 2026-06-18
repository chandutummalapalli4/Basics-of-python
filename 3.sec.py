a,b,c=map(int,input("Enter numbers :").split())
if (a>b and a<c) or (a>c and a<b):
    print("a is second largest number.")
elif (b>a and b<c) or(b>c and b<a):
    print("b is second largest number")
else:
    print("c is second largest number")