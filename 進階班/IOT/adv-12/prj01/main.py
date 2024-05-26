#########################匯入模組#########################
from machine import Pin
import time 
import mcu

#########################函式與類別定義#########################

#########################宣告與設定#########################
gpio = mcu.gpio()  # 建立GPIO物件
earthquake = Pin(gpio.D3, Pin.IN)  # 建立震度感測器物件

#########################主程式#########################
while True:
    print(earthquake.value())
    if earthquake.value() == 1:
        print("Emergency!")
    time.sleep(1)