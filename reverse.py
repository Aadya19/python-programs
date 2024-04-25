'''num=(input())
rev=0
n = 0
while num!=0:
    n = num % 10
    rev= rev * 10+n 
    num//=10

print(rev)'''
num=input()
num=num[::-1]
print(num)