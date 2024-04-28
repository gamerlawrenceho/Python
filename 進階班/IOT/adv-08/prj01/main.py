#########################匯入模組#########################
from machine import Pin, ADC
import time
import mcu
#########################函式與類別定義#########################
def on_message(topic, msg):
    global m
    msg = msg.decode("utf-8")
    m = msg
    topic = topic.decode("utf-8")
    print(f"my subscribe topic:{topic}, msg:{msg}")
#########################宣告與設定#########################
wi = mcu.wifi("SingularClass",  "Singular#1234")
wi.setup(ap_active=False, sta_active=True)
if wi.connect():
    print(f"IP={wi.ip}")
    
MQTT = mcu.MQTT("Lawrence", "mqtt.singularinnovation-ai.com", "singular", "Singular#1234")
MQTT.connect()
MQTT.subscribe("lawrence", on_message)

gpio = mcu.gpio()
LED = mcu.LED(gpio.D5, gpio.D6, gpio.D7, pwm=False)
LED.RED.value(0)
LED.GREEN.value(0)
LED.BLUE.value(0)
light_sensor = ADC(0)
m = ""
#########################主程式#########################
while True:
    MQTT.check_msg()
    light_sensor_reading = light_sensor.read()
    time.sleep(0.1)
    if m == "on":
        LED.RED.value(1)
        LED.BLUE.value(1)
        LED.GREEN.value(1)
    elif m == "off":
        LED.RED.value(0)
        LED.BLUE.value(0)
        LED.GREEN.value(0)
    elif m == "auto":
        if light_sensor_reading > 700:
            LED.RED.value(1)
            LED.BLUE.value(1)
            LED.GREEN.value(1)
        else:
            LED.RED.value(0)
            LED.BLUE.value(0)
            LED.GREEN.value(0)
    time.sleep(0.1)