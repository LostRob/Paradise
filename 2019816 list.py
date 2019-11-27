# 81、举例说明SQL注入和解决方法
import re
from typing import List

input_name = 'zs'
sql = 'select * from demo where name = "%s"' % input_name
print('正常SQL语句',sql)

input_name = 'zs;drop database demo'
sql = 'select * from demo there name = "%s"' % input_name
print('SQL注入语句',sql)

# 82、用正则切分字符串输出

s = 'info:xiaoZhang 33 shandong'
res = re.split(r":| ",s)
print(res)

# 83、正则匹配163.com结尾邮箱

# ret = re.match('[\w]{4,20}@163\.com$',email)

# 84、递归求和

def get_sum(num):
    if num >= 1:
        sum = num + get_sum(num - 1)
    else:
        sum = 0
    return sum

a = get_sum(10)
print(a)

# 85、python字典和json字符串相互转化

# 86、

# 87、 res = str.count('张三')

# 88、字符串大小写转换

agg = 'ADAdjaksjaddADJAIDJI'
print(str.upper(agg))
print(str.lower(agg))

str1 = 'hello world ha ha'
res1 = str1.replace(' ','')
print(res1)

list1= str1.split(' ') #具体split()方法
print(list1)
res2 = ''.join(list1)
print(res2)

# 90、正则匹配不是以4和7结尾的手机号
tels = ['13565345123','18912344321','10086','18888888887','13152790320']
for tel in tels:
    pipei = re.match('1\d{9}[0-3,5-6,8-9]',tel)
    if pipei:
        print('（不以47结尾）的（手机号）：%s' % pipei.group())  # % tel
    else:
        print('%s 不符合要求' % tel)

# 91、引用计数算法

# 92、int报错

# 93、列举3条PEP8编码规范

# 94、正表达式匹配第一个URL ？

# 95、正则匹配中文

title = '你好，hello，世界，世界，你好，世'
pattern = re.compile(r'[\u4e00-\u9fa5]+')  #见正则表达式re.compile()方法
result = pattern.findall(title)

print(result)

# 96、简述乐观锁和悲观锁

# 97、文件打开模式

# 98、linux命令重定向
# >表示输出 会覆盖文件原有内容
# >>表示追加 会将内容追加到已有文件的末尾

# 99、正则表达式匹配出<html><h1>www.itcast.cn</h1></html>

# ret = re.match(r'<\w*><\w*>.*?</\2></\1>',label)

# 100、python传参数是传值还是传址？ 见收藏

# 101、求两个列表的交集并集差集

x = set('runoob')
y = set('google')
print(x,y)
print(x & y)
print(x | y)
print(x - y)

# 102、生成0-100的随机数

import random

frr1 = 100 * random.random()
frr2 = random.randint(1,100)
frr3 = random.choice(range(1,101))

print(frr1)
print(frr2)
print(frr3)
print(frr1+frr2+frr3)

# 103、lambda匿名函数好处
# 精简代码，lambda省去了定义函数，map省去了for循环过程

a = ['苏州','','中国','','过程','德国','日本','美国','']
frrr = list(map(lambda x:'empty' if x == '' else x,a))
print(frrr)

# 104、常见网络传输协议

# UDP TCP HTTP FTP


# 105、单引号双引号三引号用法

print('she said "yes" ')

# 106、垃圾回收机制
# 引用计数

# 107、HTTP请求中get和post区别

# 108、python中读取excel文件的方法
# 引用数据分析库pandas、

# 109、简述多线程、多进程

# 110、python正则中search和match

s = '小明年龄18岁 工资10000'

res = re.search(r'\d+',s).group()
print('search结果',res)

res = re.findall(r'\d+',s)
print('findall result',res)

res = re.match('小明',s).group()
print('match result1',res)

res = re.match(r'\d+',s).group()
print('match result2',res)

res = re.match('工资',s).group()
print('match result3',res)
