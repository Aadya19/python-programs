class circle:
    def __init__(self,r):
        self.r=r
    def printing(self):
        area=3.14*r*r
        print("area of circle is" , area)
class rectangle :
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def printing(self):
        area1=l*b
        print("area of rectangle is ", area1)
l=float(input())
b=float(input())
r=float(input())
o=circle(r)
o1=rectangle(l,b)
o.printing()
o1.printing()