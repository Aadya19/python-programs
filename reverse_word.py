s=input()
def reverse(s) :
    word=s.split()
    rev=word[::-1]
    res=' '.join(rev)
    return res
result=reverse(s)
print(result)