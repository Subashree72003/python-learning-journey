#1  EXCEPTION HANDLING
"""
try:
    a = 10
    b = 0
    print(a/b)
except:
    print("Something went wrong.")


#2
try:
    a = 10
    b = 0
    print(a/b)
except ZeroDivisionError:
    print("Something went wrong.")  """
from sys import exception

#3..............................................................................................
"""
try:
    a = 10
    b = 0 
    print(a/b)
except exception as e:
    print("Something went wrong.")
"""
#4____________________________________________ MULTIPLE EXCEPTION
"""
try:
    a = int(input("Enter a number: "))
    b = int(input("Enter a number: "))
    result = a / b
    print(result)
except ZeroDivisionError:
    print("cannot divide by zero")
except ValueError :
    print("Please enter a number") 
#5
try:
    a = int(input("Enter a number: "))
    b = int(input("Enter a number: "))
except (ZeroDivisionError , ValueError):
    print("ERROR OCCURRED")

#6 TELLS WHAT ERROR OCCURRED
try:
    num=int("hello")
except ValueError as e:
    print(e) """

#7
"""
try:
    print(a)
except Exception as ex:
    print(ex)

"""

##############################################TRY,EXCEPT,ELSE,FINALLY
"""
try:
    a=int(input("Enter a number: "))
    b=int(input("Enter a number: "))
    c=(a/b)

except ZeroDivisionError:
    print("Cannot divide by zero")

except ValueError :
    print("Please enter a number")
else:
    print(c)
finally:
    print("succesfully finally executed")

try:
    print(a)

except ZeroDivisionError:
    print("Cannot divide by zero")

except ValueError :
    print("Please enter a number")
else:
    print(a)
finally:
    print("succesfully finally executed")
"""
#_________________________________Raise exception

#1
"""
try:
    num=int(input("Enter a number: "))
    if num<0:
        raise ValueError("number can't be negative")
    print(num)
except ValueError as e:
    print(e)
    
#2
try:
    num = int(input("Enter a number: "))
    if num<18:
        raise ValueError("age cant be less than 18")
    print(num,"YOUR AGE IS ELIGIBLE FOR VOTE")
except ValueError as e:
    print(e)
    """

#........C.C.CC.C.C.
class ageerror(Exception):
    pass
try:
    num = int(input("Enter a number: "))
    if num<18:
        raise ageerror("age cant be less than 18")
    print("eligible for voting")
except ageerror as e:
    print(e)









