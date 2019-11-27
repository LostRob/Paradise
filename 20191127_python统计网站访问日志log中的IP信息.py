'''
PYTHON统计网站访问日志log中的IP信息，并排序，打印排名靠前的IP及访问量
https://blog.csdn.net/ctrigger/article/details/100019570
'''

ipdict = {}

file = open('access_2019-08-22.log')

for line in file.readlines():
    ip = line.split()[0]

    if ip in ipdict:
        ipdict[ip] = ipdict[ip] + 1
    else:
        ipdict[ip] = 1

data = sorted(list(ipdict.items()),key=lambda x:x[1] , reverse=True)

for d in data[:1000]:
    print(d[1],':\t',d[0],sep='')