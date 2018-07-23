def double(arg):
    print('Before: ', arg)
    arg += arg
    print('After: ', arg)


def change(arg):
    print('Before: ', arg)
    arg.append('More data')
    print('After: ', arg)
