#program to perform comination and permutation
#factorial(n), comb(n,r), perm(n,r) are already defined in the standard math module

def fact(n):
    if n<1: return 1
    else: return n*fact(n-1)

def fact2(n):
    value=1
    if n<1:return value
    else:
        for pars in range(1,n+1,1):                #mostly using fact2 because recursion is slower
            value *= pars
        return value

def nCr(n,r):
    if r>n: return 0
    elif r<0 or n<0: return NaN#not a number
    else:
        return fact2(n)/(fact2(r)*fact2(n-r))

def nPr(n,r):
    if r>n: return 0
    elif r<0 or n<0: return NaN#not a number
    else:
        return (fact2(n)/fact2(n-r))


