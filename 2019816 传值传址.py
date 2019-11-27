import copy

a=[1,[1,2],3]
b=copy.copy(a)
a[1].append(4)
print (a,b)
a.append(4)
print(a,b)

# 当列表或字典参数里面的值是列表或字典时，copy并不会复制参数里面的列表
# 或字典，这时就要用到deepcopy了

import copy
c=[1,[1,2],3]
d=copy.deepcopy(c)
c[1].append(4)
print (c,d)