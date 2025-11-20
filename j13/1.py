# args
# params
def sum_number(*a):
    """
    lst = []
    while True:
        a = int(input())
        if a == -1:
            break
        else:
            lst.append(int(a))
        # --------------
        lst = list(map(int, input().split()))
    """
     
    return sum(a)


print(sum_number(1, 2))