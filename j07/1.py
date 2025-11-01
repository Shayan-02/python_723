c = 50

# i = 5
# while i > 0:
#     g = int(input())

#     if c == g:
#         print("bordi")
#         break
#     elif c > g:
#         print("bozorgtar vared kon")
#     else:
#         print("koochektar vared kon")
#     i -= 1
# else:
#     print("bakhti")


for i in range(1, 6):
    g = int(input())

    if c == g:
        print("bordi")
        break
    elif c > g:
        print("bozorgtar vared kon")
    else:
        print("koochektar vared kon")
else:
    print("bakhti")