a = input()

t = 1
# valid = ["a", "e", "i", "o", "u"]
for i in range(0, len(a), 1):
    if a[i] == "a" or a[i] == "e" or a[i] == "i" or a[i] == "o" or a[i] == "u":
    # if a[i] in valid:
        t *= 2

print(t)