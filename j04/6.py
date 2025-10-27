a = int(input())

if a == 0:
    print("zero")
else:
    if a % 2 == 0 and a >= 0:
            print("even and possetive")
    if a % 2 == 0 and a < 0:
            print("even and negative")
    else:
        if a % 2 == 1 and a >= 0:
            print("odd and possetive")
        if a % 2 == 1 and a < 0:
            print("odd and negative")