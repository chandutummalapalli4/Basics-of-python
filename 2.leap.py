'''2. Leap Year (Strict Logic)
👉 Must use correct rule:
divisible by 4
not by 100 unless also by 400'''
yr=int(input("Enter a year :"))
if (yr % 4 == 0 and yr % 100 != 0) or (yr%400==0):
    print("Leap Year")
else:
    print("Not Leap Year")