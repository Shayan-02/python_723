valid = [10**x for x in range(0, 101)]

# valid = []

# for i in range(101):
#     valid.append(10**x)

# valid = list(map(lambda x: 10 ** x, [x for x in range(101)]))

a = int(input())
op = input()
b = int(input())

if a in valid and b in valid:
    if op == "+":
        print(a + b)
    elif op == "*":
        print(a*b)