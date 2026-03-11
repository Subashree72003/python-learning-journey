#____________________________________if else
#  check odd or even
"""
a= int(input("enter a"))
b= 2

if(a%b==0):
    print("a is even")
else:
    print("a is odd")  """

#--------------------------------------------
#check a number divided by 5 and 3
"""
a= int(input("enter a"))


if( a%5==0 and a%3==0):
    print("yeeyy ! it divide by both 3 and 5")
else:
    print("ohno ! it  does'nt divide by both 3 and 5")

"""
#------------------------------------------------------
#            user name login
"""
a= input(" enter the password")

if(a=="subaaa"):
    print("you are allowed to enter")
else:
   print("you are allowed to enter")  """

#------------------------------------------------------------------------
     #       traffic sign speed
"""
a=int(input("enter the speed"))
if(a>=90):
    print("you are going on high speed !!!!")
else:
    print("your speed is fine")
"""
#________________________________________________________________________
  # check password lengths
"""
a=input("enter the password")
if(len(a)>=8):
    print("your password is strong ")
else:
    print("your password is weak")
"""
#____________________________________________________________________
#  e-commerce discount
'''
a=int(input("enter the price"))
if(a>=5000):
    print("you are allowed to get discount for 10%")
else:
    print("sorry! you cant get discount ")
    '''

#---------------------------------------------------------------------
########################################################################################################--------------

#__________________________________elif
######################################################################################################################

#---------------- 1)calculator:
"""
a = int(input("enter the value for a ="))
b = int(input("enter the value for b ="))
c = input("enter the operator or operation to calculate =")

if(c=="+" or c=="add"):
    print(a+b)
elif(c=="-" or c=="sub"):
    print(a-b)
elif(c=="*" or c=="multiply"):
    print(a*b)
elif(c=="/" or c=="divide"):
    print(a/b)
elif(c=="%" or c=="mod"):
    print(a%b)
else:
    print(a**b)
"""
#----------------------------------2)traffic signal system
"""
a=input("enter the color")
if(a=="red"):
    print("you are allowed to enter")
elif(a=="yellow"):
    print(" ohh no ! walk fasttt!!!!")
else:
    print("you are not allowed to enter")
    """
#______________________________________3)season find
"""
a=int(input("enter the details to know abt the season : "))
if(a=="Rain"):
    print("It is rainy season")
elif(a=="hot"):
    print("It is summer season")
elif(a=="snow"):
    print("It is winter season")
else:
    print("it is spring season")
"""

#_________________________________________________


###################################################################################################################
          #----------------------nested if___________________________________________________________________________

# greatest among 3
a=5
b=7
c=9


#______________________________________________________________________________________
# username login
a=input("enter the username")
b=input("enter the password")
c="SUBAA!!!"
d="secret"
if(a==c):
    if(b==d):
    print("you are allowed to enter")
    else:
    print("you are not allowed to enter please check the password")
else:
    print("you are not allowed to enter please check the username")

