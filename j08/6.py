b = ""
while 1:
    a = int(input())
    if a == 0:
        break
    else:
        b += str(a)

b = b[::-1]
for i in b:
    print(int(i))