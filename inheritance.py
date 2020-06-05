class A:
    def method1(self):
        print('This is Class A, Method1')

    def method2(self):
        print('This is Class A, Method2')


class B:
    def method3(self):
        print('This is Class B, Method3')

    def method2(self):
        print('This is Class B, Method2')

# Python Does Support Multiple Inheritance


class C(A, B):
    pass


# a = A()
# a.method1()
c = C()
c.method2()
