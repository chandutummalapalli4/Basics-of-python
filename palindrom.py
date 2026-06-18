str1 = input("Enter a string: ").replace(" ", "").lower()
str2 = str1[::-1]

if str1 == str2:
    print("Palindrome")
else:
    print("Not Palindrome")