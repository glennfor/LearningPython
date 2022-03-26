'''1. Write a class called Investment with fields called principal and interest. The constructor
should set the values of those fields. There should be a method called value_after that
returns the value of the investment after n years. The formula for this is p(1 + i)n, where p is
the principal, and i is the interest rate. It should also use the special method __str__ so that
printing the object will result in something like below:
Principal - $1000.00, Interest rate - 5.12%'''

class Investment:
    def __init__(self, principal, interest):
        self.principal, self.interest = principal, interest
    def value_after(n):
        return self.principal*(1 + self.interest)**n
   
myinvest = Investment(1000, 5.12)
print(myinvest)

'''
2. Write a class called Product. The class should have fields called name, amount, and price,
holding the product’s name, the number of items of that product in stock, and the regular
price of the product. There should be a method get_price that receives the number of
items to be bought and returns a the cost of buying that many items, where the regular price
is charged for orders of less than 10 items, a 10% discount is applied for orders of between
10 and 99 items, and a 20% discount is applied for orders of 100 or more items. There should
also be a method called make_purchase that receives the number of items to be bought and
decreases amount by that much.'''

class Product:
    def __init__(self, name, amount, price):
        self.name=name
        self.amount=amount
        self.price = price

    def get_price(self, number):
        return self.price*number
    def make_purchase(self, number):
        discount = 0 if number < 10 else 0.1 if 10<=number<100 else 0.2
        return self.get_price(number)-self.get_price(number)*discount

prod = Product("Automobiles", 1200, 12000)
print(prod.make_purchase(20))



'''3. Write a class called Password_manager. The class should have a list called old_passwords
that holds all of the user’s past passwords. The last item of the list is the user’s current password.
There should be a method called get_password that returns the current password
and a method called set_password that sets the user’s password. The set_password
method should only change the password if the attempted password is different from all
the user’s past passwords. Finally, create a method called is_correct that receives a string
and returns a boolean True or False depending on whether the string is equal to the current
password or not.'''

class Password_manager:
    def __init__(self, old_passwords):
        self.old_passwords = old_passwords[:]
        self.current_password = old_passwords[-1]
    def get_password(self):
        return current_password
    def set_password(self, new_password):
        if self.is_correct(new_password):
            self.old_passwords.append(new_password)
    def is_correct(self, password):
        return True if password not in self.old_passwords else False

my_olds = ['algol68b5', 'montypython', 'shiboleth', 'my@#$$pass--word', '#1do34sed', 'multafigura']

my_manager = Password_manager(my_olds)

for _ in range(4):
    my_manager.set_password(input('Enter your new password: '))

print(my_manager.old_passwords)



'''4. Write a class called Time whose only field is a time in seconds. It should have a method called
convert_to_minutes that returns a string of minutes and seconds formatted as in the following
example: if seconds is 230, the method should return '5:50'. It should also have
a method called convert_to_hours that returns a string of hours, minutes, and seconds
formatted analogously to the previous method.'''


class Time:
    def __init__(self, time_in_secs):
        self.time = time_in_secs
    def convert_to_mins(self):
        return f'{self.time//60} : {self.time%60}'
    def convert_to_hours(self):
        return f'{self.time//3600}: {(self.time//3600)//60} : {self.time%60}'

my_time = Time(230)
yours = Time(86400)
print(my_time.convert_to_mins())
print(yours.convert_to_hours())



'''5. Write a class called Wordplay. It should have a field that holds a list of words. The user
of the class should pass the list of words they want to use to the class. There should be the
following methods:
• words_with_length(length)— returns a list of all the words of length length
• starts_with(s)— returns a list of all the words that start with s
• ends_with(s)— returns a list of all the words that end with s
• palindromes()— returns a list of all the palindromes in the list
• only(L)— returns a list of the words that contain only those letters in L
• avoids(L)— returns a list of the words that contain none of the letters in L'''

class Wordplay:
    def __init__(self, list_of_words):
        self.words = list_of_words
    def words_with_length(self, length):
        return [word for word in self.words if len(word)==length]
    def starts_with(self, s):
        return [word for word in self.words if s.lower()==word[:len(s)].lower()]
    def ends_with(self, s):
        return [w for w in self.words if w[-len(s):].lower() == s.lower()]
    def palindromes(self):
        return [w for w in self.words if w[:].lower()==w[::-1].lower()]
    def only(self, L):
        ret=[]
        for w in self.words:
            for letter in w :
                if letter not in L:
                    break
            else:
                ret.append(w)
        
        return ret
    def avoids(self, L):
        return [w for w in self.words if w not in self.only(L)]

word_list = ['only', 'green', 'mom', 'dad', 'Rotor', 'Racecar', 'tictactoe' , 'concurrency', 'Clang' , 'Monty', 'Python',
             'Javascript', 'Java', 'Idle', 'interpreter','compiler', 'Assembly', 'Google', 'Facebook', 'NASA', 'Twitter',
             'Microsoft', 'Apple', 'Sportify', 'GitHub', 'Fortran', 'Computer', 'Software', 'Engineering', 'Developer',
             'Code', 'Program', 'Application', 'Debugging','Run', 'Test', 'Optimisation', 'Programmer', 'OOP', 'Japan',
             'USA', 'China', 'UK', 'Canada', 'France', 'UAE', 'Geneva', 'Moscow', 'Bamenda', 'New York', 'London']
letters = ['o', 'a','e', 'm', 'd', 'k', 'u', 's', 'i', 'l', 'f']

my_list = Wordplay(word_list)

print(my_list.words_with_length(7))
print(my_list.starts_with('co'))
print(my_list.ends_with('er'))
print(my_list.palindromes())
print(my_list.avoids(letters))#gpn
print(my_list.only(letters))#om



    
        






    




