print()
print('Enter the answers to the following questions:')
from random import randint

for count in range(1, 11):
    x=randint(2,20)
    y=randint(2,30)
    ans=eval(input(f'Question {count}: {x} x {y} = '))
    if ans==x*y:
        print('Correct!!!')
    else:
        print(f'Wrong! The answer is {x*y}')
