#Functions
#1}26.	Write a function to add two numbers.
"""

def sum(a,b):
    print( "sum is ",a+b)


sum(5,9)


#2}27.	Write a function to subtract two numbers.
def sub(a,b):
    print( "sub is ",a-b)

sub(89,56)

#3].28.	Write a function to multiply two numbers.
def multi(a,b):
    print("multipliction of both numbers are",a*b)

multi(78,4)

#4 29.	Write a function to divide two numbers
def divide(a,b):
    print( "divide is ",a/b)

divide(78,4)

#5 30.	Write a function to find the square of a number.
def square(a):
    print( "square is ",a*a)

square(4)

#6}31.Write a function to check whether a number is even or odd.
def oddeven(a):
    if a%2==0:
        print( "It is even",a)
    else:
        print( "It is odd",a)
oddeven(78)

#7}32.Write a function to find the largest of two numbers.
def largest(a,b):
    if a>b:
        print( "largest is ",a)
    else:
        print( "largest is ",b)

largest(78,4)
"""
#8}33.	Write a function to count vowels in a string.

def vowels(a):
    for i in a:
        if i  in "aeiou":
            print( "vowel is ",i)
            count=count+1
            print(count ,"is the count of vowels")
vowels("apple")

#9}34.	Write a function to reverse a string.
def reverse_string(a):
    rev = ""
    for i in a:
        rev = i + rev
    print("Reverse string:", rev)

reverse_string("apple")


