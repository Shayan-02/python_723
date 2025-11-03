n = int(input())

a = input()
b = input()

c = 0
for i in range(n):
    if a[i] != b[i]:
        c += 1

print(c)