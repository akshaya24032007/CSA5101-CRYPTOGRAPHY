
text = input("Enter text: ").upper()
key = input("Enter key: ").upper()

for i in range(len(text)):
    c = (ord(text[i]) - 65 + ord(key[i % len(key)]) - 65) % 26
    print(chr(c + 65), end="")

