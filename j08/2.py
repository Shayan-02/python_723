a = input()
# b = ""

# for i in range(len(a) - 1, -1, -1):
#     b += a[i]

# print("YES" if a == b else "NO")

print("YES" if a == a[::-1] else "NO")