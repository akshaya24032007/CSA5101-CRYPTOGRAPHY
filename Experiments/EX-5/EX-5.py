a, b = 5, 8
s = input("Enter text: ").upper()
for ch in s:
    if ch.isalpha():
        print(chr((a*(ord(ch)-65)+b)%26+65), end="")
    else:
        print(ch, end="")
