items1 = list(map(lambda x: x ** 2, filter(lambda x: x % 2, range(1, 10))))
items2 = [x ** 2 for x in range(1, 10) if not x % 2]

print(items1)
print(items2)

# 例子：输出函数执行时间的装饰器。
from functools import wraps
from time import time
'''
def record_time(func):
    """自定义装饰函数的装饰器"""

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        print(f'{func.__name__}: {time() - start}秒')
        return result

    return wrapper
'''

# 如果装饰器不希望跟print函数耦合，可以编写带参数的装饰器。

def record(output):
    """自定义带参数的装饰器"""

    def decorate(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start = time()
            result = func(*args, **kwargs)
            output(func.__name__, time() - start)
            return result

        return wrapper

    return decorate