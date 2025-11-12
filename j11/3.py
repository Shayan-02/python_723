print("hello world")


# voroodi nadarad khorooji nadarad
def sayHello1():
    print("hello world")


# voroodi darad khorooji nadarad
def sayHello2(name):
    print("hello", name)

# voroodi nadarad khorooji darad
def sayHello3():
    # return "hello world3"
    y = 50
    return y

# voroodi darad khorooji darad
def sayHello4(name):
    return f"hello {name} "

# n = input()
sayHello1()
sayHello2(input())
print(sayHello3() * 2)
print(sayHello4("reza")* 2)
