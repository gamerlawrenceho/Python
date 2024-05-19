#########################匯入模組#########################
from machine import Pin, I2C
import dht
import time
import mcu
import json 
import ssd1306 
from machine import ADC 

#########################函式與類別定義#########################

#########################宣告與設定#########################
gpio = mcu.gpio()  # 建立GPIO物件
wi = mcu.wifi("SingularClass", "Singular#1234")  # 建立WIFI物件
wi.setup(ap_active=False, sta_active=True)  # 設定WIFI模組
if wi.connect():
    print(f"IP={wi.ip}")  # 連接到伺服器

mqtt_client = mcu.MQTT("lawrence", "mqtt.singularinnovation-ai.com", "singular", "Singular#1234") # 建立MQTT客戶端
mqtt_client.connect() # 建立MQTT客戶端

i2c = I2C(scl=Pin(gpio.D1), sda=Pin(gpio.D2))  # 建立I2C物件
oled = ssd1306.SSD1306_I2C(128, 64, i2c)  # 建立OLED物件
d = dht.DHT11(Pin(gpio.D0, Pin.IN)) # 建立 DHT11 物件
msg_json = {} # 建立字典
light_sensor = ADC(0)  # 建立 ADC 物件

#########################主程式#########################
while True:
    d.measure()  # 讀取溫溼度
    temp = d.temperature()  # 將溫溼度分別存在不同變數
    hum = d.humidity()  # 將溫溼度分別存在不同變數
    oled.fill(0)  # 清除螢幕
    oled.text(f"Humidity: {hum:02d}", 0, 0) # 顯示文字, x座標, y座標
    oled.text(f"Temperature: {temp:02d}{'\u00b0'}C", 0, 10) # 顯示文字, x座標, y座標
    oled.show()  # 顯示螢幕
    msg_json["humidity"] = hum # 將溫溼度存在字典中
    msg_json["temperature"] = temp # 將溫溼度存在字典中
    msg_json["light_sensor"] = light_sensor.read() # 將光感度存在字典中
    msg = json.dumps(msg_json) # 將字典轉換成JSON格式
    mqtt_client.publish("lawrence", msg) # 發送MQTT訊息
    time.sleep(1)