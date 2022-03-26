#implement caesar's cipher
#it is well simple to implement and it uses the idea of ASCII character codes
#Note that in Python,characters are encoded in UNICODE by default

#The idea behind this encryption is to shift indvidual x-ters in a string(message) by a certain number(the key)
#White spaces are not encrypted 

from string import whitespace as wsp, punctuation as punc,ascii_lowercase as lower, ascii_uppercase as upper

def encrypt(plain_text, key):
    cipher = ''
    for char in plain_text:
        if not char.isascii():
            cipher += char
        elif char.islower():
            cipher += lower[(lower.index(char)+key)%26]
        elif char.isupper():
            cipher += upper[(upper.index(char)+key)%26]
        elif char in punc:   #char.ispunct():
            cipher = punc[(punc.index(char)+key)%26]
        else: cipher += char  # for whitespaces etc        
    return cipher

def decrypt(cipher, key):
    original_text = ''
    for char in cipher:
        if not char.isascii():
            original_text += char
        if char.islower():
            original_text += lower[(lower.index(char)-key)%26]
        elif char.isupper():
            original_text += upper[(upper.index(char)-key)%26]
        elif char in punc:   #char.ispunct():
            original_text = punc[(punc.index(char)-key)%26]
        else: original_text += char  # for whitespaces etc        
    return original_text


def mainfunc():
    while True:
        choice = input("\n>>>Encrypt(E/e) or Decrypt(D/d) or Quit(Q/q)?\n").lower()[0]
        if choice == 'e':
            print("Enter text to encypt:")
            text = input()
            key = int(input('Enter an encryption key between(0 and 26):  '))
            print('\nThe encrypted text is {}'.format(encrypt(text, key)))
        elif choice == 'd':
            print("Enter cipher text to decypt:")
            text = input()
            key = int(input('Enter an encryption key:  '))
            print('\nThe encrypted text is {}'.format(decrypt(text, key)))
        elif choice == 'q':
            break;
        else:
            print('Invalid Choice !!!!\a\a\a\a')

if __name__ == '__main__':
    mainfunc()
