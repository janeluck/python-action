import os

path = os.getcwd()
filenames = os.listdir(path)


def first_lower(s):
    if len(s) == 0:
        return s
    else:
        return s[0].lower() + s[1:]


for filename in filenames:
    os.rename(filename, first_lower(filename))
