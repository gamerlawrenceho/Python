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


#########################宣告與設定#########################
client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION2)
client.on_publish = on_publish
client.username_pw_set("singular", "Singular#1234")
client.connect("mqtt.singularinnovation-ai.com", 1883, 60)
client.loop_start()
os.environ["OPENAI_API_KEY"] = getpass.getpass()
model = ChatOpenAI(model="gpt-4o", temperature=0.2)
#########################主程式#########################
while True:
    ans = input("請輸入想跟AI說的話: ")
    msg = model.invoke(
        [
            HumanMessage(
                content="""
    你是一個負責開燈跟關燈的管理員
    'ON'代表開燈
    'OFF'代表關燈
    'None'代表不要做任何事
    你只能根據使用者的回應來決定要回答'ON'或'OFF'或'None'
    不能回答其他的字串
                """
            ),
            HumanMessage(content=ans),
        ]
    ).content
    print(msg)
    result = client.publish("lawrence_AI", msg)  # 發布訊息
    result.wait_for_publish()  # 等待發布完成

    # 檢查發布是否成功
    if result.rc == mqtt.MQTT_ERR_SUCCESS:
        print("Message published successfully")
    else:
        print("Failed to publish message")
    time.sleep(0.1)