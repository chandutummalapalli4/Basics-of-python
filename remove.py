s = input("Enter a string: ")

result = "".join(filter(str.isalpha, s))

print(result)