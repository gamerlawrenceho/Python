#########################匯入模組#########################
from machine import Pin
from time import sleep

#########################函式與類別定義#########################

#########################宣告與設定#########################
p2 = Pin(2, Pin.OUT)

#########################主程式#########################
while True:
    p2.value(0)
    sleep(1)
    p2.value(1)
    sleep(1)