"""
輸入三角形三邊(存入變數a, b, c中) 
判斷是否能構成三角形(利用邊長運算進行判斷，可以上網搜尋公式)
是三角形:則顯示面積和周長
不是:則顯示，無法構成三角形
​
三角形面積公式:
p = 1/2 (a+b+c)
area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
​
EX:
a = 3 
b = 4
c = 5
周長:12.0
面積:6.0 
​
a = 1
b = 10
c = 100
無法構成三角形
"""
from contextlib import AbstractAsyncContextManager
from re import A
from this import d

a = float(input("邊長1:"))
b = float(input("邊長2:"))
c = float(input("邊長3:"))
d = a + b + c
if a + b > c and b + c > a and a + c > b:
    p = 1 / 2 * (a + b + c)
    area = (p * (p - a) * (p - b) * (p - c))**0.5
    print(f'周長{d}')
    print(f'面積{area}')
else:
    print('無法構成三角形')