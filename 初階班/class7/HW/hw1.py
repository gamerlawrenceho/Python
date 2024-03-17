import random as r

a = 100
b = 0
x = r.randrange(0, 101)
while True:
    ans = int(input(f"請輸入{b}~{a}的整數:"))
    if ans > x:
        print('在小一點')
        if b < ans < a:
            a = ans
    elif ans < x:
        print('在大一點')
        if b < ans < a:
            b = ans
    else:
        print('~恭喜猜中了!~')
        break