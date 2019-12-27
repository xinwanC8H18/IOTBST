#Basics
print("Hello World")
example_dict={"liaobin":20, "yujing":18, "jiansheng":16}
print(example_dict["yujing"])
 
#if elif else Structure
if example_dict["liaobin"]>20:
    example_dict["yujing"]=example_dict["yujing"]+1
    print("Yujing + 1")
elif example_dict["liaobin"]<20:
    example_dict["yujing"]=example_dict["yujing"]-1
    print("Yujing - 1")
else:
    print("Nothing happened")
 
#for in Loop
for i in [1,2, [3,4],"life"]:
    print(i)
 
for i in range(3):
    print(i, "Hello for")
 
#while Loop
while i<5:
    print(i, "Hello while")
    i = i+1
 
#Function Definitation
def square_sum(a,b):
    """Return the square sum of two parameters"""
    a=a**2
    b=b**2
    return a+b
 
print(square_sum(1,2))
print(square_sum(b=2,a=1))
 
#package and unpackage
def package_position(*all_parameters):
    print(type(all_parameters))
    print(all_parameters[0])
    print(all_parameters[-1])
 
package_position(1,4,6)
 
def package_keyword(**all_parameters):
    print(type(all_parameters))
    print(all_parameters)
 
package_keyword(a=1,b=3,c=5)
 
def unpackage(a,b,c):
    print(a)
    print(b)
    print(c)
 
pkg_tuple=(5,6,7)
pkg_dict={"a":5,"b":6,"c":7}
unpackage(*pkg_tuple)
unpackage(*pkg_dict)
unpackage(**pkg_dict)
 
#Module
from first import laugh
 
for i in range(2):
    laugh()


#Module
def laugh():
    print("Ha")
 
def big_laugh():
    print("HaHaHa")
