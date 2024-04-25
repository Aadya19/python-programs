def fun(l,ind):
    try:
        a=l.copy()
        a[10]=l[0]/l[ind]
    except ValueError:
        print("value error")
    finally :
        print("end of fun")
l=[1,2,3,4,5]
try :
    fun(l,5)
except IndexError:
    print("index error")
finally :
    print("end of function")