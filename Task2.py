# task 1
#1 positive or negative
"""a = int(input("Enter a number: "))
if(a<0):
    print("the number is negative")
else:
    print("the number is positive")
#2 odd or even
a = int(input("Enter a number: "))
b = int(input("Enter b number: "))
if(a%b==0):
    print("the number is even")
else:
    print("the number is odd")"""
#3 largest of 2 numbers
"""a = int(input("Enter a number: "))
b = int(input("Enter b number: "))
if(a>b):
    print(" A is greater than B")
else:
    print(" B is greater than a") """
#4}largest of 3 numbers using if condition
"""
a = int(input("Enter a number: "))
b = int(input("Enter b number: "))
c = int(input("Enter c number: "))
if(a>b and a>c):
    print(" A is greater")
elif(b>c and b>c):
    print(" B is greater")
else:
    print(" C is greater")"""
"""
#5}check whether a number is divisible by 5 and 11
a = int(input("Enter a number: "))
if(a%5==0 and a%11==0):
    print("the number is divisible by 5 and 11")
else:
    print("the number is not divisible by 5 and 11")
"""
#6]	Write a program to check whether a year is a leap year.
"""
year = int(input("Enter the year: "))
if(year%400==0 or year%4==0 and year%100!=0 ):
    print("the year is leap year")
"""
#7	Write a program to check whether a character is vowel or consonant.

"""a = input("enter a character")
vowel = "aeiouAEIOU"

for i in a:
    if i in vowel:
        print(i," is a vowel")
    else:
        print(i," is not a vowel, it is  a consonant")
"""

## find vowels from a word
"""b=input("Enter a value :")
a="A,E,I,O,U,a,e,i,o,u"

for i in b:
    if i in "aeiou":
        print(i)"""
#8.check whether a number is multiple of 3 and 7
"""
a=int(input("Enter a number :"))
if (a%3==0 and a%7==0):
    print("the number is divisible by 3 and 7")
else:
    print("the number is not divisible by 3 and 7") """

#9.	Write a program to check whether a number is a three-digit number or not

"""input =int(input("Enter a number :"))
print(len(str(input)))
if len(str(input))==3:
    print("the number is 3 digit")
else:
    print("the number is  not a  3 digit ")"""

#10.check whether a number is greater than 100.
input =int(input("Enter a number :"))
if input>100:
    print("the number is greater than 100")
else:
    print("the number is less than 100")















