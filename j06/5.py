i = 1
while i <= 20:
    if i % 6 == 0 and i >= 15:
        break
    elif i % 7 == 0:
        i += 2
        continue
    else:
        print(i)
    i += 1
