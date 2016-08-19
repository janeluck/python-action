from collections import Iterable
import myos

a1 = 100
if a1 > 0:
    print('python')
# b = input() or 20
if int(10) < 20:
    print('young')
else:
    print('modest')

sum = 0
for x in range(101):
    sum = sum + x
print(sum)

# tuple
c = (1, 2, 3)
print(c)

# list
d = [1, 2, 3]
print(d)

# dict
e = {'jane': 25, 'jack': 29, 'rose': 31}

# set 要创建一个set，需要提供一个list作为输入集合(自动过滤掉重复的key)
f = set([1, 2, 3, 4, 5, 1, 5])
print(f)

# g = set([2, 3, 4, 5, d]) unhashable type: 'list'

# & |

print(set([1, 2, 3]) & set([2, 3, 4]))
print(set([1, 2, 3]) | set([2, 3, 4]))


# function
def h():
    pass


def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x > 0:
        return x
    else:
        return -x


def my_xy(x, y):
    return x + 1, y + 1


h1, h2 = my_xy(2, 3)
print(h1)
print(h2)
print(my_xy(5, 6))


def my_xn(x, n):
    s = 1
    while n:
        n -= 1
        s = s * x

    return s


print(my_xn(3, 5))


# default argument, 定义默认参数要牢记一点：默认参数必须指向不变对象
def my_xyz(x, y=2, z=3):
    return x, y, z


print(my_xyz(1))
print(my_xyz(5, z=99))


# 可变参数量 *
# calculate a*a + b*b + ......
def my_calc(*numbers):
    sum = 0
    for x in numbers:
        sum += x * x
    return sum


j = [2, 3, 4, 5, 6, 7]
print(my_calc(*j))


def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)


person('jane', 25, city='Beijing')
extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, **extra)


# 命名关键字参数可以有缺省值
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)


def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)


args = (1, 2, 3)
kw = {'d': 88, 'x': '#'}
f2(*args, **kw)


# recursion
def k(n):
    if n == 1:
        return 1
    return n * k(n - 1)


k(10)
# slice
m = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(m[:4])
print(m[-4: -1])
print(m[:-4])
print(m[-4])
print(m)

# iteration
print(isinstance('abc', Iterable))
for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)

# list Comprehensions
print([x * x for x in range(1, 11)])

print([m + n for m in 'ABC' for n in 'XYZ'])

print([d for d in myos.listdir('./')])

L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s, str)]
print(L2)


# generator

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'


for n in fib(6):
    print(n)

print('-----------------------')
# Python的for循环本质上就是通过不断调用next()函数实现的
for x in [1, 2, 3, 4, 5]:
    pass

# 首先获得Iterator对象:
it = iter([1, 2, 3, 4, 5])
# 循环:
while True:
    try:
        # 获得下一个值:
        x = next(it)
        print(x)
    except StopIteration:
        # 遇到StopIteration就退出循环
        break

print(list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])))

# 匿名函数
list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9]))


# 类
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))


Student('jane', 25).print_score()


# private


class Lesson(object):
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name


print(Lesson('Math').get_name())


# Polymorphism
class Animal(object):
    def run(self):
        print('Animal is running...')


class Dog(Animal):
    def run(self):
        print('Dog is running...')

    def eat(self):
        print('Eating meat...')


class Teacher(object):
    name = 'Teacher'


class Student1(object):

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2016 - self._birth

s3 = Student1()
s3.birth = 1999
print(s3.age)



