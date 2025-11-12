# args
# params
def sum_number(*a):
    # s = 0
    # while True:
    #     a = int(input())
    #     if a == 0:
    #         break
    #     else:
    #         s += a
    # return s
    s = 0
    # for i in a:
    #     s += i
    # return s
    for i in range(len(a[0])):
        s += a[0][i]
    return s

print(sum_number([1, 2, 3, 4, 5]))