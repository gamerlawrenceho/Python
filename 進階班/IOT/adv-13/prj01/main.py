import getpass
import os

os.environ["OPENAI_API_KEY"] = getpass.getpass()

from langchain_openai import ChatOpenAI

model = ChatOpenAI(model="gpt-4o", temperature=5)
from langchain_core.messages import HumanMessage

while True:
    ans = input("請輸入想跟AI說的話: ")
    print(
        model.invoke(
            [
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
    )