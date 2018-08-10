def myfunc(*args):
    for a in args:
        print(a, end=' ')
    if args:
        print()
    print()

myfunc(10, 50, 'Ayoub EL HAKIMI', 21, 30)

def myfunc2(**kwargs):
    for k, v in kwargs.items():
        print(k,v, sep=' -> ')
    if kwargs:
        print()

info = {'Name': 'Ayoub EL HAKIMI', 'Age': 26, 'Country' : 'Morocco'}

myfunc2(**info)
