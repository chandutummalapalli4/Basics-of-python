str1 = input("Enter a string: ")

result = ""

for ch in str1:
    if 'A' <= ch <= 'Z':
        result += chr(ord(ch) + 32)
    else:
        result += ch

print("Lowercase:", result)