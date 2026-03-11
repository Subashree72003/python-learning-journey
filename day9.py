# 1} print odd numbers
"""
for i in range(1,51):
    if i % 2 == 0:
        continue
    print(i)
"""
#2} skip vowles in string

"""a = "python program"

for i in (a):
    if (i  in ["a","e","i","o","u"]):
        continue
    print(i)
"""
#3]skip negtative numbers

"""a=[10,-5,20,-3,30,-90]
for i in a:
    if(i<0):
        continue
    print(i) """
#4}print divisible by 5 from 1 to 50
"""for i in range(1,51):
    if(i%5 !=0):
        continue
    print(i) """
    


#_____________________break____________________________________
#1}check a number is prime or not
a= 5
for i in (2,a):
    if(a%i==0):
        break
    print(i ,"is prime")


