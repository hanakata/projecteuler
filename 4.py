a, b, p = 999, 999, 0
while a > 100:
    n = a * b
    string = str(n)
    if string == string[::-1]:
        if p < int(string):
            s = a
            v = b
            p = int(string)
        if b == 100:
            b = 999
            a -= 1
        else:
            b -= 1
    else:
        if b == 100:
            b = 999
            a -= 1
        else:
            b -= 1
print("a:"+str(s)+"b:"+str(v)+"A:"+str(p))
