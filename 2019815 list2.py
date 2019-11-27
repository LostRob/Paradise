# 52
list = [2,3,5,4,9,6,7,3,2]

list.append(12)
print(list)

new_list = []

def get_min(list):
    # 获取列表最小值
    a = min(list)
    # 删除最小值
    list.remove(a)
    # 判断是否重复
    if a not in new_list:
        # 将最小值加入新列表
        new_list.append(a)
    if len(list) > 0:
            get_min(list)
    return new_list

new_list = get_min(list)
print('new_list = {}'.format(new_list) )


theList = ['a','b','c']
if 'a' in theList:
    print ('a is in the list')

if 'd' not in theList:
    print ('d is not in the list')

# 54、保留两位小数

# 55、三个方法打印结果
def fn(k,v,dic={}):
    dic[k] = v
    print(dic)

fn('one',1)
fn('two',2)
fn('three',3,{})
# fn("one",1）直接将键值对传给字典；
# fn("two",2)因为字典在内存中是可变数据类型，所以指
# 向同一个地址，传了新的额参数后，会相当于给字典增加键值对
# fn("three",3,{})因为传了一个新字典，所以不再是原先默认参数的字典

# 56、常见状态码及意义

# 57、从前端、后端、数据库阐述web项目的性能优化

# 58、使用pop和del删除字典中的name字段，dic = {'name':'zs','gae':'18'}
dic = {'name':'zs','age':'18'}
dic.pop('name')
print(dic)

dic = {'name':'zs','gae':'18'}
del dic['name']
print(dic)

# 59、列出常见Mysql数据存储引擎

# 60、zip
print('='*10 + 'zip()函数单个参数' + '='*10)
list1 = [1, 2, 3, 4]
tuple1 = zip(list1)
#print('tuple1 = {}' .format(tuple1))
print('zip()函数的返回类型：', type(tuple1))#类型为
# list2=list(tuple1)

# 60、dict()创建字典新方法

# 61、同源策略

# 62、cookie和session的区别

# 63、简述多线程、多进程

# 64、简述any()和all()方法
# any():只要迭代器中有一个元素为真就为真
# all():迭代器中所有的判断项返回都是真，结果才为真
# python中什么元素为假？
# 答案：（0，空字符串，空列表、空字典、空元组、None, False）

# 65、Error分别代表什么异常

# 66、python追踪copy和deepcopy的区别

# 67、列出几种魔法方法并简要介绍用途

# 68、命令行启动程序并传参

# 69、改成生成器
#     生成器是特殊的迭代器
#     列表表达式的[]改成()即可变成生成器

# 70、使用a.strip()去除收尾空格
t123 = 'hehehe'
t123.strip()
print(t123)

# 71、距离sort和sorted对列表的排列
# sort 在list基础上修改，无返回值
# sorted有返回值，是新的list

# 72、对list排序foo

# 73、使用lambda函数对list排序foo = [-5,8,0,4,9,-20,-2,8,2,-4]

foo = [-5,8,0,4,9,-4,-20,-2,8,2,-4]
to1 = sorted(foo,key = lambda x:(x<0,abs(x)))
print(to1)

