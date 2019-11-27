list = [1,2,3,4,5]

def fn(x):
    return x ** 2


fnl = map(fn,list)
fnl = [i for i in fnl if i > 10]
print(fnl)


import random
import numpy

a = random.randint(10,20)
b = numpy.random.randn(5)
c = random.random()
print(a,b,c)


# datetime 模块
import datetime
a = str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')) + ' 星期' + str(datetime.datetime.now().isoweekday())
print(a)

# raise自定义异常

def fn():
    try:
        for i in range(5):
            if i > 2:
                raise Exception('数字大于2.')
    except Exception as ret:
        print(ret)
fn()

# 1行代码展开列表 得出[1,2,3,4,5,6]

a = [[1,2],[3,4],[5,6]]
x = [j for i in a for j in i]
print(x)

import numpy as np
b = np.array(a).flatten().tolist()
print('b =',b)

# 输出2和3的N次幂表 还有另外的写法 见runoob/python3输入和输出

for x in range(1,120):
    print('{0:2d}|{1:3d}|{2:4d}'.format(x,2**x,3**x))

x = 'abc'
y = 'def'
z = ['d','e','f']


m = x.join(y)
n = x.join(z)
print(m)
print(n)

