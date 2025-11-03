a = [1, 2, 3, "ali", "reza", True, None]

b = [4, 5, 6]

# print(a)

# for i in range(len(a)):
    # print(a[i], end=" ")

# for i in a:
#     if type(i) == bool:
#         print(i, end=" ")

a.append("salam")

a.insert(0, "mohammad")

# a.append(b)

# print(a[-1])

# for i in b:
#     a.append(i)

a.extend(b)

# print(len(a))

for i in a:
    print(i, end=" ")

print()

a.remove("mohammad")

a.pop(3)
a.remove(3)
a.pop()
a.clear()
# del a

for i in a:
    print(i, end=" ")
