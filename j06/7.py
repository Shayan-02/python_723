# i = 1
# while i < 21:
#     print(i)
#     i += 1

# for i in range(1, 31, 2):
#     if i == 25:
#         break
#     elif i % 3 == 0 and i % 5 == 0:
#         continue
#     else:
#         print(i, end="\t")

i = 1
while i < 31:
    if i == 25:
        break
    elif i % 3 == 0 and i % 5 == 0:
        i += 2
        continue
    else:
        print(i, end="\t")
        i += 2