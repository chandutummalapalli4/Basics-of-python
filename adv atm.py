'''If withdraw > balance → "Insufficient balance"
If withdraw not multiple of 100 → "Invalid amount"
If balance after withdrawal < 1000 → "Maintain minimum balance warning"
Else → "Transaction successful'''
bal=int(input("Enter bank balance:"))
wi=int(input("Enter withdraw amount:"))
if wi>bal:
    print("Insufficient balance")
elif wi %100!=0:
    print("Invalid amount")
elif (bal-wi)<1000:
    print("Maintain minimum balance warning")
else:
    print("Transaction successful")