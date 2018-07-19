""" First Test """

def search4vowels(word):
    """ Return boolean based on any vowels found.  """
    vowels = set('aeiou')
    found =  vowels.intersection(set(word))
    return bool(found)
print(search4vowels('ayoub'))
print(search4vowels('sky'))

""" Second Test """

def search4vowels(word):
    """Return any vowels found in a supplied word."""
    vowels = set('aeiou')
    return vowels.intersection(set(word))
found = search4vowels('ayoub')
print(found)
found = search4vowels('Sky')
print(found)

""" Third Test : Annotations PEP 3107 """

def search4vowels(word:str) -> set:
    """ Return any vowels found in a supplied word."""
    vowels = set('aeiou')
    return vowels.intersection(set(word))
found = search4vowels('ayoub')
print(found)
found = search4vowels('Sky')
print(found)



