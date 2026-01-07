n = int(input())

# fact = 1
# for i in range(1, n + 1):
#   fact *= i

# print(fact)

def fact(num):
  if num == 1:
    return 1
  else:
    return fact(num - 1) * num


def fib(num):
  if num == 1 or num == 2:
    return 1
  else:
    return fib(num - 2) + fib(num - 1)


# print(fact(n))
print(fib(n))