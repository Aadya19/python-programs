class a:
    def fun1(self):
        print("f1")
    def fun2(self):
        print("f2")
class b(a):
    def __init__(self) -> None:
        print("1")
    def __init__(self)->None:
        print("2")
    def fun3(self):
        print("f3")
    def fun4(self):
        print("f4")
class c(b):
    def fun5(self):
        print("f5")
o=a()
p=b()
q=c()
p.fun1()
q.fun5() 
'''inherites b class function oly'''
#only child class has acccess to inherite parent class methods
#parent class inherites its own methods only 