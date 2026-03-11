
var1 = "Dhoni"
print(var1, "is my captian")
#_________________________________________________________________________
var1 ="Dhoni"
var2 = 150
print(var1,"scored",var2,"runs")
#_____________________________________________________________________________________
var1 = "Ramesh"
var2 ="Suresh"
print(var1, "and",var2 ,"are best friends") # is used for single line comments
#___________________________________________________________

""" :raise
"""




#2nd method with% ===================______________++++++++++++++___________________

var1 = "Dhoni"
print("%s is my captain"  %(var1))

#______________________________________________________________
var1 ="Dhoni"
var2 = 150
print("%s scored %d runs" %(var1,var2))

#_______________________________________________________________

var1 = "Ramesh"
var2 ="Suresh"
print("%s and %s are best friends" %(var1,var2))

#______________________________________________________________________


# 3rd method  with {}
var1 = "Dhoni"
print ("{} is my captain" .format(var1))

var1 ="Dhoni"
var2 = 150
print("{} scored {} runs".format(var1,var2))







#+india scored +350 runs in +50 overs against +pakisthan in +1996

var1="india"
var2= 350
var3= 50
var4= "pakisthan"
var5= 1996
print(var1,"scored",var2, "runs in ", var3,"overs against ", var4,"in", var5)


#____________________________________________________________________

#____________________________slicing________________________
var1 = "Besant tech"
print(var1[3:9])          #__________

#__________in negative and positive in note





#________________________________________ data type and length_________________________________p0

a= 10
print(type(a))

a ="Besant"
print(type(a))
print(len(a))


#_______________________________type casting
#immmutable int to string
# directa cahnge panna mudiyathu oru variablela store pani tha panna mudiyum

a = 1234
print(type(a))
b=str(a)
print(type(a))
print(len(b))

# ______________string methods

#a.lower()
#a.upper()
#a.title()
#a.capitalize()
#a.swapcase()
   # no arguments passed inside()

name1 = "BESANT TECH 123"
name2 = "BeSant Tech"
print(name1.lower())    #ellamey low akum
print(name2.lower())
print(name1.upper())     # ellamey upp akum
print(name2.upper())
print(name1.title())
print(name2.title())     # 1st letter and space aprm vara letter caps
print(name1.capitalize())
print(name2.capitalize()) # 1st letter matu caps
print(name1.swapcase())
print(name2.swapcase())   # lower goes upper and upper goes lower

