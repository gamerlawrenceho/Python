import requests
import datetime
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import os
from pytube import YouTube  # pip install -U pytube


def call_weather_api(lon: str = "121.5319", lat: str = "25.0478") -> dict:
    """ 使用OpenWeatherMap API獲取天氣資訊 """
    api_key = "892da2f13edf3c7f382637760e72d224"
    base_url = "https://api.openweathermap.org/data/2.5/onecall?"
    exclude = "minutely,hourly"  # 不要分鐘級和小時級的資料
    units = "metric"
    lang = "zh_tw"
    send_url = base_url
    send_url += "lat=" + lat
    send_url += "&lon=" + lon
    send_url += "&exclude=" + exclude
    send_url += "&appid=" + api_key
    send_url += "&units=" + units
    send_url += "&lang=" + lang

    response = requests.get(send_url)  # 發送請求，獲得天氣資訊
    info = response.json()  # 將json格式轉換為字典
    return info


def get_plot_fig(xlist, ylist, title, xlabel, ylabel) -> plt.Figure:
    """建立圖表"""
    # 獲取當前模組所在的目錄
    module_dir = os.path.dirname(os.path.abspath(__file__))
    # 計算圖片的絕對路徑
    font_path = os.path.join(module_dir, 'TaipeiSansTCBeta-Bold.ttf')
    font = FontProperties(fname=font_path, size=14)
    fig, ax = plt.subplots()
    ax.plot(xlist, ylist)
    ax.set_xlabel(xlabel, fontproperties=font)
    ax.set_ylabel(ylabel, fontproperties=font)
    ax.set_title(title, fontproperties=font)

    return fig


def save_weather_icon(icon_code):
    icon_url = f"https://openweathermap.org/img/wn/{icon_code}@2x.png"
    response = requests.get(icon_url)
    with open(f"{icon_code}.png", "wb") as icon_file:
        icon_file.write(response.content)


def get_7_Days_weather(info: dict):
    """獲取七天天氣資訊, 回傳日期和溫度的list"""
    dates = []
    temps = []
    for i in range(7):
        temp = info["daily"][i]["temp"]["day"]
        time = datetime.datetime.fromtimestamp(
            info["daily"][i]["dt"]).strftime("%m/%d")
        dates.append(time)
        temps.append(temp)
    return dates, temps


#######################取得影片資訊########################
def get_video_info(url: str):
    """取得影片資訊，依序回傳:影片的標題、作者、長度、縮圖網址、解析度"""
    yt = YouTube(url)  # 建立YouTube物件
    title = yt.title  # 取得影片的標題資訊
    author = yt.author  # 取得影片的作者資訊
    length = yt.length  # 取得影片的長度資訊
    image_url = yt.thumbnail_url  # 取得影片的縮圖網址

    # 篩選progressive代表影片有音訊與影像, file_extension='mp4'代表影片格式為mp4
    streams = yt.streams.filter(progressive=True, file_extension='mp4')
    res = []  # 用於儲存所有解析度
    for stream in streams:
        res.append(stream.resolution)

    return title, author, length, image_url, res


#######################下載影片########################
def download_video(url: str, r: str):
    """下載影片，回傳:是否下載成功(True/False)"""
    yt = YouTube(url)  # 建立YouTube物件
    streams = yt.streams.filter(progressive=True, file_extension='mp4')

    res = []  # 用於儲存所有解析度
    for stream in streams:
        res.append(stream.resolution)

    # 判斷解析度有沒有在目前的streams裡面
    if r in res:
        # 取得該解析度的串流
        stream = streams.filter(res=r)[0]
        stream.download()  # 下載影片
        return True
    else:
        return False