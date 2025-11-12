def fibonachi(number):
    lst = [1, 1]
    if number == 1:
        return 1
    elif number == 2:
        return 1
    else:
        fib =  fibonachi(number - 1) + fibonachi(number - 2)
        return fib
        # return lst
    # fib = 0
    # f1, f2 = 1, 1
    # for i in range(3, number + 1):
    #     f3 = f1 + f2
    #     f1, f2 = f2, f3
    #     lst.append(f3)
    # return lst

print(fibonachi(6))
print(type(fibonachi(6)))

# for i in fibonachi(6)[::-1]:
#     print(i)