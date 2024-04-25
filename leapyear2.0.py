year=int(input())
'''if year%4==0 :
    if a%100==0 :
       if year%400==0 :
           print("century leap year")
       else :
          print("century year but not leap year")
    else :
        print("leap year")
else :
    print("normal year")'''

'''if year%100==0 and year%400==0 :
    print("leap year")
elif year%100!=0 and year%4==0 :
    print("leap year")
else :
    print("not a leap year")'''

if year%400==0 or year%100!=0 and year%4==0 :
    print ("leap year")
else :
    print ("not a leap year")