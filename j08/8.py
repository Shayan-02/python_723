lst = []

while True:
    n = int(input())
    if n == 0:
        break
    else:
        lst.append(n)
    

print(sum(lst))