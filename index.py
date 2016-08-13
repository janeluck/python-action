a = 100
if a > 0:
    print('python')
#b = input() or 20
if int(10) < 20 :
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
e = {'jane': 25, 'jack': 29, 'rose': 31 }

# set 要创建一个set，需要提供一个list作为输入集合(自动过滤掉重复的key)
f = set([1, 2, 3, 4, 5, 1, 5])
print(f)

# g = set([2, 3, 4, 5, d]) unhashable type: 'list'

