def factorial(n):
    # fact = 1
    # for i in range(1, n + 1):
    #     fact *= i
    #     print(fact)
    # return fact
    fact = 1
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)
a = int(input())
print(f"factorial: {factorial(a)}")