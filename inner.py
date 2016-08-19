from datetime import datetime
from collections import deque
import hashlib
print(datetime(2016, 10, 1, 8, 30))
print(datetime.now())
q = deque(['a', 'b', 'c'])
q.appendleft('x')
q.append('y')
print(q)

md5 = hashlib.md5()
md501 = hashlib.md5()

md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
print(md5.hexdigest())
md5.update('in python hashlib?'.encode('utf-8'))
print(md5.hexdigest())





