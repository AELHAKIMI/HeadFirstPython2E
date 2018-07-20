def search4vowels():
    """ Return a bolean based on any vowels found. """
    vowels = set('aeiou')
    word = input('Provide a word to search for  vowels: ')
    found = vowels.intersection(set(word))   
    print(found)

def search4letters(phrase:str , letters:str = 'aeiou') -> set:
    """ Return a set of the 'letters' found in 'phrase'. """
    return set(letters).intersection(set(phrase))
