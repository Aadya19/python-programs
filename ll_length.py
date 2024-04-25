class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.count=None
class sll:
    def __init__(self):
        self.head=None
    def first_insert(self,data):
        if self.head ==None:
            self.head=node(1)
        else:
            new=node(data) 
            new.next=self.head
            self.head=new
    def printing(self):
        if self.head==None:
                return
        i=self.head
        while i:
            print(i.data)
            i=i.next
    def length(self):
        len=0
        current=self.head
        while current:
            len+=1
            current=current.next
        return len        
l=[1,2,3,4,5]
o=sll()
for i in l:
    o.first_insert(i)
o.printing()
print(o.length())