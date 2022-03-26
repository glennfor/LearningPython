# working with strings

phrase="Software Engineering is cool"
print(phrase+"and I am in")
print(phrase.upper())#convert to upper case
print(phrase.lower())#convert to lower csase
print("Is the phrase uppercase: " +str(phrase.isupper()))#boolean values have to beconverted befors concatenatin wth a string
print("Is the phrase now in lowercase : " +str(phrase.upper().islower()))#false of course
print("The phrase \"" + phrase + "\" has " +str(len(phrase) )+" characters")#convert to string first
print(phrase.index("E"))
print(phrase.index("a"))
print(phrase.index("cool"))
print(phrase.replace("cool", "amazing"))