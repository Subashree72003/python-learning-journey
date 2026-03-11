#_________________________________________________scope of variable
#local variable__________________________
"""def demo():
    x=10
    print(x)

demo()
"""

#Global variable_________________________________
"""x=50
def demo2():
    print(x)

demo2()


# non- local__________________________________________
def outer():
    x =20 # x is enclose variable
    def inner():
        print(x)

    inner()
outer()    """

#Global Keyword_______________________________________________
"""x=5
def change():
    global x
    x = 10
change()
print(x)

#non local keyword__________________________________________________
def outer():
    x =20
    def inner():
        nonlocal x
        x = 10
        inner()
        print(x)
    outer()
"""



###################################TASK############################################################
#1]PASS 2 ARGUMENTS AND FIND ODD AND EVEN
"""def oddeven(num1,num2):
    for i in (num1 ,num2) :
        if i%2==0:
            print(i,"is even")
        else:
            print(i,"is odd")

oddeven(2,7)
"""
#2}pass 2 values and do arithmetic operations
"""def arithmetic(num1,num2):
    for i in (num1,num2) :
        if a=="+":
            print(i) 





arithmetic( 5,2 ) """

#3}reverse  A String
"""a = "python"
rev =" "      """"""
for i in a:
        rev=i+rev
        print(rev) """

#3}reverse  A String by passing arguments
rev="  "
def revstrng(a):
    for i in (a):
        rev=i+rev
        print(rev)

revstrng("python")





