try:
    x = int(input())
except ValueError:
    print("مقدار وارد شده معتبر نیست")
else:
    print("عدد وارد شده معتبر است:", x)