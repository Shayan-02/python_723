def sayName():
    global name, family
    family = "ahmadi"
    d = 20
    name = "ali"
    return name

print(sayName())
print(name, family)
print(d)