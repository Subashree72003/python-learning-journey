"""
a=["hello",2,3]
print(sorted) """
"""
a = ['apple','kiwi','banana']
res = sorted(a,key = lambda x:len(x))
print(res)

"""
"""add = lambda a,b: a+b
print(add (2,3))
print(add(5,7))
print(add(10,20))"""
"""
a =[10,"apple",5.5]
print(sorted(a,key = lambda x :str(x)))
"""
"""
a=[10,"apple",5.5,"banana",2]
print(sorted(a,key = lambda x :str(x)),x)))
"""
"""
data = {"john":85,"emi":92,"sam":78}
print(sorted(data))
print(sorted(data.items(),key = lambda x :x[1])) #value based sort
print(sorted(data.items(),key = lambda x :x[0])) #key based sort """
#1 to find max number

a=[1,8,9,4,16,78]






print(max(a,key = lambda x : str(x)))
#2 to print divisible by 7
a=[35,11,8,14,3,9,7,28,9]
res = list(filter(lambda x : x %7==0 ,a))
print(res)

