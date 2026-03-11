# loops
#1 print numbers from 1 to 10
"""for i in range(1,11):
    print(i)

#2print even numbers from 1 to 50
for i in range(1,51):
    if i % 2 == 0:
        print(i,end = " ")
#3 sum of numbers from 1 to 100.
a=0
for i in range(1,101):
    a=a+i
    print(a) """
from itertools import count

#4 multiplication table of a number
"""a = 0
for i in range(2,11):
    a= 2*i

    print("2 X" ,i, "=",a) """
"""
#5 count numbers in a list
a = [2,3,4,5,6,7,8]
for i in a:
    print(count(i))  """

#6} print all elements in a list using a for loop
"""a =[ "a","b","c","d","e","f","g","h","i","j"]
for i in a:
    print(i ,end = "  ")"""

# 7}count vowels in a string.
"""a = "beautiful"
count = 0
for i in a:
    if i in "aeiou":
        print(i,end = " " )
        count += 1

print( "the count is " ,count)
"""
#8 print numbers in reverse order from 10 to 1.
#a.
"""a = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
for i in range(len(a) - 1, -1, -1):
    print(a[i], end=" ")

#b slicing
for i in a:
    print(a[::-1])

#c reverse key word
for i in  reversed(a):
    print(i)
#d while
b = 10
while b <=-1:
    print(b)
    b +=1

#e without using  variable
for i in range (11,0,-1):
    print(i)
    
#9 find factorial of a number using for loop

b = 1
for i in  range (1,6):
    b= b*i
    print(b) """

# 10 find the largest number in a list.
"""
current_number = 2
a = [2,4,6,16,8,40]
for i in a:
    if i>current_number:
        current_number = i
print(current_number)

# 11) count the number of digits in a number
a=int(input("enter the number :"))
a= str(a)
if len(a)==2:
    print(a," is a 2 digit")
elif len(a)==3:
    print(a," is a 3 digit")
elif len(a)==4:
    print(a," is a 4 digit")
else:
    print(a," is a 5 digit") """

#12) print square of numbers from 1 to 10.
"""
a = 1
for i in range(1,11):
    b=i*i
    print(b," is the square of ",i)

#13]print cube of numbers from 1 to 10.
for i in range(1,11):
    b=i*i*i
    print(b," is the cube of ",i) """

#14 find sum of elements in a list
a=[5,9,6,7,3,8]
print(sum(a))








