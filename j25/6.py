class Test:
    __x = 10
    y = 20
    def chap(self):
        print(self.__x)
    def variz(self, mablagh):
        self.__x += mablagh
    def bardasht(self, mablagh):
        self.__x -= mablagh

t1 = Test()
t1.chap()
t1.y = 30
print(t1.y)
t1.__x = 30
print(t1.__x)
t1.chap()
t1.variz(50)
t1.bardasht(20)
t1.chap()
