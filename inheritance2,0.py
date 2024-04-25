class ab:
    branch="cse"
    def __init__(self,a) -> None:
        ab.x=10
        self.a=a
    def fun(self):
        print("fun1",self.branch,self.x)
        print("fun,ab.branch,ab.x")
o=ab(3)
o.fun()