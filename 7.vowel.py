L = input("Enter a letter: ")

if len(L) != 1:
    print("Invalid input")
elif L.lower() in ("a", "e", "i", "o", "u"):
    print("Vowel")
else:
    print("Consonant")