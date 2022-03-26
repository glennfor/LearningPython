
def isvowel(ch):
    if ch.lower() in ['a','e', 'i', 'o','u']:
        return True
    return False

def translate(phrase):
    fin=''
    for char in phrase:
        if isvowel(char):
            fin+='g'
        else: fin+=char
    return fin


print("Enter a text to translate to giraffe language:\n")
string=input('> ')
print('Translated text is:')

print(translate(string))
