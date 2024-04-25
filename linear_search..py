si=0
li=len(l)-1
se=9
while si<li:
    mid=(si+li)/2
    if l[mid]==se:
        print("element found")
        break
    else:
        li=mid-1
else:
    print("element not found")

'''time complexity
n/2^1
n/2/2=n/4=n/2^2
n/2^3
....
k=> n/2^k=1
n=2^k
log2(n)=log2(2^k)
log2(n)=k*log2(2)
k=log2(n)   ''' 