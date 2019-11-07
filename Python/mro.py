    class A:
        def m(self):
            print("this is A")

    class B:
        def m(self):
            print("this is B")    

    class C(B,A):
        def ma(self):
            print("this is C")

    c = A()
    c.m()