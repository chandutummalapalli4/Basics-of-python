'''1. Take input number and digit to remove
2. Extract digits one by one from the number
3. Check each digit:
   - If digit is NOT equal → keep it
   - If equal → skip it
4. Build a new number using kept digits (this will be in reverse order)
5. Reverse the result to get correct order
6. Print final number'''

num=int(input("Enter a Value:"))
value=int(input("Enter Value To Remove:"))
temp=num
result=0
while num>0:
    digits=num%10
    num//=10
if  digits==value:
    continue
else: 
        print("Digits:",digits)
        result=result*10+digits
        print("Result:",result)