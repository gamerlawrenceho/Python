#########################匯入模組#########################
import paho.mqtt.client as mqtt  # 匯入MQTT模組 pip install paho-mqtt
from langchain_openai import ChatOpenAI  # 匯入ChatOpenAI模組
import time  # 匯入time模組
import getpass  # 匯入getpass模組
import os  # 匯入os模組
from langchain_core.messages import HumanMessage  # 匯入HumanMessage模組


#########################函式與類別定義#########################
def on_publish(client, userdata, mid, reason_code, properties):
    print(f"Message {mid} has been published.")


#########################宣告與設定#########################
client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION2)  # 建立MQTT客戶端
client.on_publish = on_publish  # 設定on_publish函式
client.username_pw_set("singular", "Singular#1234")  # 設定用戶名和密碼
client.connect("mqtt.singularinnovation-ai.com", 1883, 60)  # 連接到伺服器
client.loop_start()  # 開始循環
os.environ["OPENAI_API_KEY"] = getpass.getpass()  # 輸入OpenAI API Key
model = ChatOpenAI(model="gpt-4o", temperature=0.5)  # 建立ChatOpenAI物件

#########################主程式#########################
while True:
    ans = input("請輸入想跟AI說的話: ")
    msg = model.invoke([
                HumanMessage(
                    content="""
    你是一個負責開燈跟關燈和開柵欄的AI
    你要能根據使用者的回應來決定要回答'ON'或'OFF'或"NONE"的回答
    也能根據使用者的回應來決定要回答'開柵欄'或'關柵欄'或"NONE"的回答
    你必須回答'ON'或'OFF'及'開柵欄'或'關柵欄'
                """
                ),
                HumanMessage(content=ans), 
            ]
    ).content
    print(msg)  # 打印回應  
    result = client.publish("lawrence", msg)  # 發布訊息
    result.wait_for_publish()  # 等待發布完成

    if result.rc == mqtt.MQTT_ERR_SUCCESS:
        print("Message published successfully")  # 發布成功
    else:  
        print("Failed to publish message")  # 發布失敗
    time.sleep(0.1)  # 等待一秒

