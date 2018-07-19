def search4vowels():
    vowels = set('aeiou')
    word = input('Provide a word to search for  vowels: ')
    found = vowels.intersection(set(word))   
    print(found)
search4vowels()
