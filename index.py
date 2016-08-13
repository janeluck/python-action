a = 100
if a > 0:
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