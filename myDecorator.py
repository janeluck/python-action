def bread(func):
    def wrap():
        print("<------->")
        func()
        print("<------->")

    return wrap


def ingredients(func):
    def wrap():
        print("#tomatoes#")
        func()
        print("~salad~")

    return wrap


@bread
@ingredients
def sandwich():
    print("---ham---")


sandwich()
