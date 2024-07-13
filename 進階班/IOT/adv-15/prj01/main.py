#########################匯入模組#########################
import paho.mqtt.client as mqtt
import time
import getpass
import os
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage


#########################函式與類別定義#########################
def on_publish(client, userdata, mid, reason_code, properties):
    print(f"Message {mid} has been published.")

def on_connect(client, userdata, connect_flags, reason_code, properties):
    print(f"連線結果:{reason_code}")
    client.subscribe("hello_home")  # 訂閱主題


def on_message(client, userdata, msg):
    global home_config
    print(f"我訂閱的主題是:{msg.topic}, 收到訊息:{msg.payload.decode('utf-8')}")
    home_config = str(msg.payload.decode("utf-8"))

#########################宣告與設定#########################
# client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION2)  # 建立MQTT客戶端
# client.on_publish = on_publish  # 設定MQTT客戶端的回檔函式
# client.username_pw_set("singular", "Singular#1234")  # 設定MQTT客戶端的用戶名和密碼
# client.connect("mqtt.singularinnovation-ai.com", 1883, 60)  # 連接MQTT客戶端
# client.loop_start()  # 開始循環
os.environ["OPENAI_API_KEY"] = getpass.getpass()  # 設定OpenAI API Key
model = ChatOpenAI(model="gpt-4o", temperature=0.2)  # 建立OpenAI API物件
home_config = """
{"humidity": 0, "temperature": 1000, "lightsensor": 0}
"""
#########################主程式#########################
while True:
    ans = input("請輸入想跟AI說的話: ")  # 輸入用戶要跟AI說的話
    msg = model.invoke(
        [
            HumanMessage(
                content="""
                你是一個負責開燈跟關燈的管理員
                'ON'代表開燈
                'OFF'代表關燈
                'None'代表不要做任何事
                'home_config'代表使用者正在關心家裡狀況
                你只能根據使用者的回應來決定要回答'ON'或'OFF'或'None'或'home_config'
                不能回答其他的字串
                """
            ), 
            HumanMessage(content=ans), 
        ]
    ).content  # 將訊息轉換成字串
    print(msg)
    if msg == "home_config":
        msg = model.invoke(
        [
            HumanMessage(
                content="""
                你是一個負責解釋家裡狀態的小幫手, 你只能回答100個字, 
                感測器位置沒有問題, 光感應器數值越大代表越暗, 數值範圍在0~1023之間, 
                有問題請解釋可能發生災難或狀況, 
                家裡感測器不可能壞掉喔!, 目前家裡的狀態是:
                """
            ), 
            HumanMessage(content=home_config), 
        ]
        ).content  # 將訊息轉換成字串
        print(msg)  # 顯示訊息

    # result = client.publish("lawrence_AI", msg)  # 發布訊息
    # result.wait_for_publish()  # 等待發布完成

    # # 檢查發布是否成功
    # if result.rc == mqtt.MQTT_ERR_SUCCESS:  # 如果發布成功
    #     print("Message published successfully")
    # else:
    #     print("Failed to publish message")
    time.sleep(0.1)