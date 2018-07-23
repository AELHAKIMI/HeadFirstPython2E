""" First Test """

def search4vowels(word):
    """ Return boolean based on any vowels found.  """
    vowels = set('aeiou')
    found =  vowels.intersection(set(word))
    return bool(found)
print(search4vowels('ayoub'))
print(search4vowels('sky'))

""" Second Test """

def search4vowels2(word):
    """Return any vowels found in a supplied word."""
    vowels = set('aeiou')
    return vowels.intersection(set(word))
found = search4vowels('ayoub')
print(found)
found = search4vowels('Sky')
print(found)

""" Third Test : Annotations PEP 3107 """

def search4vowels3(word:str) -> set:
    """ Return any vowels found in a supplied word."""
    vowels = set('aeiou')
    return vowels.intersection(set(word))
found = search4vowels('ayoub')
print(found)
found = search4vowels('Sky')
print(found)

""" Fourth Test : Data Passed by reference or by value"""

def double(arg):
    print('Before: ', arg)
    arg *= arg
    print('After: ', arg)

def change(arg):
    print('Before: ', arg)
    arg.append('More data')
    print('After: ', arg)

