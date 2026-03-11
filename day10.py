#positional argument
"""def student(name,age):
    print(name,age)

student("suba",22) """

#key word arguments-----------------------------------------------------------------------
"""def student(name,age):
    print(name,age)

student(age="suba",name =22)
"""
#default arguments________________________________________________________________________
"""def student(name = "student"):
    print("hello",name)

student() """
#variable length argument________________________________________________________________
                         #*ARGS
"""def record(*degree):
    print(degree ,"WERE THE COURSES PRESENT HERE")

record("MCA","BCA","B.E")  """

"""         #**KWARGS

def emprecord(**details):
    print(details)

emprecord(name="suba",age=22,course="MCA")
"""