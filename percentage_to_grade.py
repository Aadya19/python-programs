a=float(input("math ="))
b=float(input("sci ="))
c=float(input("hin="))
d=float(input("eng ="))
e=float(input("hist ="))
if ((a and b and c and d and e )<35) :
    print("fail")
else :
   t=(((a+b+c+d+e)/500)*100)
   if t>75 :
        print("grade A") 
   elif t>=60 and t<=74 :
        print("grade B")
   elif t>=35 and t<=59 :
        print("grade C")
   else :
        print("fail")
