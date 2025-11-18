li = [4, 1, 2, 3, 4, 8, 7, 1, 25, 9]
newli = sorted(li, key = lambda x: x%3)  # همان لیست بر میگرداند نه شیء دیگر
# newli = sorted(li)
print(newli)