#calculates total resistance in parallel for any number of resistors

#function to calculate the reciprocal

def reciprocal(x):
    if x<0: return 0#in this case reciprocal of negative numbers are considered 0 since resistance can't be negative
    elif x==0: return 0#will deal with this case in the main program
    else:
        return (1.0/x)


print("This program calculates the total resistance for any number of resistors in parallel")
print("Enter the values of the resistances:----->Enter any non-digit character(s) to stop input")
sums=0.0
find_0=False
while True:
    try:
        res=float(input(''))
    except ValueError:
        break
    else:
        if res==0:
            find_0=True
        else:
            sums +=reciprocal(res)


if find_0:
     total=0
else:
    total=reciprocal(sums)

print(f'The sum of resistances of this resistance values in parallel circuit is {total} ohms')
        
