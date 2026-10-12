s = "MONARCHYBDEFGIKLPQSTUVWXZ"
t = input("Enter text: ").upper()

for i in range(0, len(t), 2):
    a, b = t[i], t[i+1]
    x, y = s.index(a), s.index(b)
    r1, c1 = divmod(x, 5)
    r2, c2 = divmod(y, 5)

    if r1 == r2:
        print(s[r1*5+(c1+1)%5]+s[r2*5+(c2+1)%5], end="")
    elif c1 == c2:
        print(s[((r1+1)%5)*5+c1]+s[((r2+1)%5)*5+c2], end="")
    else:
        print(s[r1*5+c2]+s[r2*5+c1], end="")

