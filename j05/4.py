start = int(input("start: "))
end = int(input("end: "))

while start <= end:
    if start % 3 == 0 and start % 5:
        print(start)
    start += 1