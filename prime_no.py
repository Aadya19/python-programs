a=int(input())
for i in range(2,a) :
    if a%i==0 :
        print("not a prime number")
        break
else :
    print("a prime number")