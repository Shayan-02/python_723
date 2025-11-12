def separator(ls):
    odd = []
    even = []
    for _ in ls:
        if _ % 2 == 0:
            even.append(_)
        else:
            odd.append(_)
    return even, odd

# print(separator([1, 2, 3, 4, 5]))

# print(separator(list(map(int, input().split()))))

# a = input().split()
# b = []

# for i in a:
#     b.append(int(i))

# print(separator(b))

# x = input().split()
# x = list(map(int, x))
# print(separator(x))
# print(separator([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
# print(separator(list(map(int, input().split()))))

# a = input().split()
# b = []

# for i in a:
#     b.append(int(i))

# print(separator(b))