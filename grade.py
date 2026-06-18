a, b, c = map(int, input("Enter marks: ").split())

if a < 35 or b < 35 or c < 35:
    print("Fail")
else:
    avg = (a + b + c) / 3

    if avg >= 90:
        print("A")
    elif avg >= 75:
        print("B")
    elif avg >= 50:
        print("C")
    else:
        print("D")