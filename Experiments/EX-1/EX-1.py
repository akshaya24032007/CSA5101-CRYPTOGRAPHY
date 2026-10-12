text = input("Enter text: ")
k = int(input("Enter key: "))

for ch in text:
    if ch == " ":
        print(" ", end="")
    else:
        print(chr((ord(ch) - 65 + k) % 26 + 65), end="")

