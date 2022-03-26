#patterns in programming

print('PATTERNS DISPLAY')
print('Pattern 1: Left aligned Right Angled Rriangle(R.A.T)')
h=eval(input('Enter the height of the RAT:  '))
for i in range(h):
    print('%-*s'%( h, '*'*(i+1)))

print('Pattern 2: Right aligned Right Angled Rriangle(R.A.T)')
h=eval(input('Enter the height of the RAT:  '))
for i in range(h):
    print('%*s'%(h, '*'*(i+1)))
