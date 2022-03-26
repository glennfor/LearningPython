#quad.py
#calculates roots of a quadratic equation

import math
ans='Yes'

while ans[0]=='Y' or ans[0]=='y':  
    print('This Program determines the roots of a quadratic equation')
    print('Form of equation: ax^2 + bx + c=0 with a>0')
    print('Enter the values of the constants a, b and c')
    try:
        a=float(input(' a = '))
        b=float(input(' b = '))
        c=float(input(' c = '))
    except ValueError:
        print('Invalid -->Values must must numbers')
        exit(0)

    discriminant=(b**2)-4*a*c
    if a==0:
        print('The quadratic term must not be zero')
    else:
        if discriminant > 0:
            delta=math.sqrt(discriminant)
            print(f'Roots of the equation are: {(-b+delta)/(2*a)} and {(-b-delta)/(2*a)} ')
            print("Types of roots: Real and Distinct")
        elif discriminant==0:
            print(f'Roots of the equation are: {-b/(2*a)} repeated')
            print('Type of roots: Real and Equal(Repeated or Double)')
        else:
            delta=complex(math.sqrt(abs(discriminant)/2*a))
            print(f'The roots of the equation are: {complex(-b/(2*a), -delta)} and {complex(-b/(2*a), delta)}')
            print('Types of roots: Complex and Distinct')
    print()
    for _ in range(3):
        ans=input('Do you want to calculate again: (yes or no) >')
        if ans[0]=='Y' or ans[0]=='y' or ans[0]=='N' or ans[0]=='n':break
    else:
        print()
        print('User is a twit')
    print()
