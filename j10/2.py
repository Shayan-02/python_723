n = int(input())

# toggle
c = False
b = ""

for i in range(n):
    a = input()
    if a == "CAPS":
        c = not c
    if a != "CAPS": 
        if c == True:
            b += a.upper()
        elif c == False:
            b += a.lower()

print(b)