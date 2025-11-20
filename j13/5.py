def show_in(ls):
    for i in ls:
        print(i, end=" ")


n = list(map(int, list(filter(lambda x: int(x)>5, input().split()))))
show_in(n)