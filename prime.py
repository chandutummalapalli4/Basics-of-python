n = int(input("Enter a value: "))
count=0
if n <= 1:
    print("Not a Prime")
else:
    for i in range(2,n):
        if n % i == 0:
            print("Not a Prime")
            break
    else:
        count+=1
        print("Count:",count)
        print("Prime Number")