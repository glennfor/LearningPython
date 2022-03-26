#Prime numbers in range 1 to n
#i will use a different approach from the one in my

print('Enter anumber to get all primes in range 1 to the number')
try:
    lim=int(input(''))
except ValueError:
    print('Invalid entry')
else:
    for i in range(2,lim):
        for j in range(2,i):
            if i%j==0:
                break
        else:#if loop completed meaning no divisor
            print(i, end=' ')

print('\n')#two newline characters
print('Enter two numbers to get all primes in range of the two numbers')
try:
    lim=int(input('First number:  '))
    beg=int(input('Second number:  '))
except ValueError:
    print('Invalid entry')
else:
    maxim=max(beg, lim)
    minim=min(beg, lim)
    for i in range(minim,maxim,1):
        for j in range(2,i,1):
            if i%j==0:
                break
        else:#if loop completed meaning no divisor
            print(i, end=' ')
