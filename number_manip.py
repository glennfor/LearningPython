#dealing with numbers
#importing math module
from math import*   # * means all// this is almost equivalent to an include statement in C/C++

print("\nProgram to calculate x to the power y:")
print("1. For integers only")
x=input("Enter the base:    ")
y=input("Enter the power:  ")
z=int(x)**int(y)  #note you have to convert the types first
print(str(x)+ " ^ "+str(y) +" = "+str(z))
print("Math is DONE")
print("\n2.For any other set of number:")
x=input("Enter the base:    ")
y=input("Enter the power:  ")
print(x, " ^ ",y ," = ",float(x)**float(y))
print("Math is DONE")
