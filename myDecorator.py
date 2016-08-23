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


# @:grammar  sugar
@bread
@ingredients
def sandwich1():
    print("---ham1---")

sandwich1()


def sandwich2():
    print("---ham2---")


bread(ingredients(sandwich2))()
