c = 50
i = 0
while i <= 5:
    g = int(input(f"guess{i+1}: "))
    if c == g:
        print("you win")
        break
    elif c < g:
        print("enter lower")
    else:
        print("enter higher")
    i += 1
    print(f"you have {5 - i} another chances")
else:
    print("you loss")