a = int(input( 'a = '))
x = int(a//100)
y = int((a//10)%10)
z = int(a%10)
if (x ** 3 + y ** 3 + z ** 3) == x * 100 + y * 10 + z:
    print('是水仙花数')
else:
    print('不是水仙花数')
