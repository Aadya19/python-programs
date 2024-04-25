r=input()
'''match r:
    case 'a':
        print("vowel")
    case 'e':
        print("vowel")
    case 'i':
        print("vowel")
    case 'o':
        print("vowel")
    case 'u':
        print("vowel")
    case _:
        print("constant")'''
if r in 'aeiouAEIOU' :
    print("vowel")
else :
    print("constant")