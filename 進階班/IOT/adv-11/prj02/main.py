#########################匯入模組#########################
import time
import mcu
from machine import Pin, I2C
import ssd1306


#########################函式與類別定義#########################
def on_message(topic, msg):
    global m
    msg = msg.decode("utf-8")  # Byte to str
    topic = topic.decode("utf-8")
    print(f"my subscribe topic:{topic}, msg:{msg}")  # 打印訂閱主題與訊息
    m = msg  # 將訊息存入m變數


#########################宣告與設定#########################
gpio = mcu.gpio()  # 建立GPIO物件
i2c = I2C(scl=Pin(gpio.D1), sda=Pin(gpio.D2))  # 建立I2C物件
oled = ssd1306.SSD1306_I2C(128, 64, i2c)  # 建立OLED物件

wi = mcu.wifi("SingularClass", "Singular#1234")  # 建立WIFI物件
wi.setup(ap_active=False, sta_active=True)  # 設定WIFI模組
if wi.connect():
    print(f"IP={wi.ip}")  # 連接到伺服器

mqtt_client = mcu.MQTT("lawrence", "mqtt.singularinnovation-ai.com", "singular", "Singular#1234") # 建立MQTT客戶端
mqtt_client.connect()   # 建立MQTT客戶端
mqtt_client.subscribe("lawrence", on_message)   # 訂閱主題
m = 0 # 初始化消息
servo = mcu.servo(gpio.D8)  # 建立輪詢器物件

#########################主程式#########################
while True:
    mqtt_client.check_msg()  # 等待已訂閱的主題發送資料
    oled.fill(0)  # 清除螢幕
    oled.text(f"{wi.ip}", 0, 0)
    oled.text("topic : lawrence", 0, 10)
    oled.text(f"msg : {m}", 0, 20)
    oled.show()
    servo.angle(int(m))
    time.sleep(1)