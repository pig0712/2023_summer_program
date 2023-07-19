a = "WXYZ"
b = ""
a = list(a)
for i in range(len(a)):
    r = ord(a[i])+3

    if r >= 91:
        b += chr(r-26)

    else:
        b += chr(r)

print(b)