text = input("Enter text: ").upper()

plain = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
cipher = "QWERTYUIOPASDFGHJKLZXCVBNM"

for ch in text:
    if ch == " ":
        print(" ", end="")
    else:
        print(cipher[plain.index(ch)], end="")

