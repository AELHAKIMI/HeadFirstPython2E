def search4vowels():
    vowels = set('aeiou')
    word = input('Provide a word to search for  vowels: ')
    found = vowels.intersection(set(word))   
    print(found)
search4vowels()


def search4letters(phrase:str , letters:str = 'aeiou') -> set:
    """ Return a set of the 'letters' found in 'phrase'. """
    return set(letters).intersection(set(phrase))
#Positional Assignment
search4letters('ayoub el hakimi', 'aei')

#Keyword Assignment
search4letters(letters='aei', phrase='ayoub el hakimi')
