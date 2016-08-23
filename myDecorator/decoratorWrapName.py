import functools
def log(func):
    @functools.wraps(func)
    def wrapper():
        print('-----log-----')
        return func()
    return wrapper


@log
def printname():
    print('janeluck')


printname()



