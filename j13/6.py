from functools import reduce

li = [10, 2, 3, 4, 5]
result = reduce(lambda x,y: x**y, li) # فاکتوریل
print(result)