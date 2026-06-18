a,b,c=map(int,input("enter sides:").split())
if a+b>c and a+c>b and b+c>a:
    print("Valid Triangle")
if a==b==c:
    print("Equilateral")
elif a==b or b==c or c==a:
    print("Isosceles")
else:  
    print("Scalene")