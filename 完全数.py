for num in range(1,10000):
    y = 0
    for x in range(1,num-1):
        if num % x == 0:
            y = y + x
    if y == num:
        print(num)