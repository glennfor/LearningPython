num = 10_000_000_000
print(f'{num:,}')
friends = ['Johnn', 'James', 'Philip', 'Peter', 'Paul', 'Simon', 'Levi']
for index, friend in enumerate(friends):
    print(f'Name {index} | {friend}')

names = ['Clark Kent', 'Bruce Wayne', 'Peter Parker', 'Wade Wilson']
super_heroes = ['Superman', 'Batman', 'Spider', 'Deadpool']
universes = ['DC Comics','DC comics', 'Marvel', 'Marvel']

for name, hero , universe in zip(names, super_heroes, universes):
    print(f'{name} is actually {hero} from {universe}')

vec3d = (12, 9, 40)
*vec2d, z = vec3d
*vec2d2, _  = vec3d #ignore
print(vec3d)
print(vec2d)
print(vec2d2)

rgb_col = (133, 90, 89)
red, *blue_and_green = rgb_col
print(rgb_col)
print(red)
print(blue_and_green)
second_red, *_ = rgb_col
print(second_red)

#------------------
#test
class Person():
    pass

me = Person()
Person.name = 'P.O'
Person.hit = 'SE-CE-GM'
print(Person.name)
print(Person.hit)

#using setattr and getatrr

firstkey = 'first'
firstval = 'Carlos'
setattr(me, firstkey, firstval)

first = getattr(me, firstkey)

print(first)

person_info = {'first':'Jack', 'last':'Hunt'}
you = Person()
for key, value in person_info.items():
    setattr(you, key, value)

for key in person_info.keys():
    print(getattr(you, key))

###3#################33
#recursion
def fibonacci(n):
    if n==1 or n==2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

print()
print('FIBONACCI RECURSION')
for  i in range(101):
    try:
        print(f'{i} : {fibonacci(i)}')
    except RecursionError:
        break

#memoization
#store the values for previous funtion cals so that future funtiobns won't have to repeat the same wook


#1. implicit implementation

fib_cache = {}

def fibo(n):
    #if value is cached return it
    if n in fib_cache:
        return fib_cache[n]
    #computethe nth term
    if n==1 or n==2:
        value = 1
    elif n>2:
        value = fibo(n-1) + fibo(n-2)
    #cache new values
    fib_cache[n] = value
    return value
print('FIBONACCI IMPLICIT CACHE')
for  i in range(101):
    print(f'{i} : {fibo(i)}')


from functools import lru_cache#Last recently Used Cache
#one l;ine way to add memoizations to funtions

@lru_cache(maxsize = 1000)#size is changeable, default size = 128
def fib(n):
    if n==1 or n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)

print('FIBONACCI BUILT_IN CACHE')
for  i in range(101):
    print(f'{i} : {fib(i)}')







