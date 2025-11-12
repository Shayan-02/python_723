s1 = {1, 2, 1, 2, 3, 6}
s2 = {4, 5, 1, 2, 3}

print(len(s1), len(s2))
print(s1 | s2) # ejtma
print(s1 & s2) # eshterak
print(s1 - s2) # tafazol
print(s2 ^ s1) # delta


print("===================")

print(s1.union(s2))
print(s1.intersection(s2))
print(s1.difference(s2))
print(s1.symmetric_difference(s2))

print("===================")

print("before :", s1)
s1.intersection_update(s2)
print("after :", s1)