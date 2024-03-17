#######################匯入模組########################
from ttkbootstrap import *
import os
import sys
from Lawrence.Lawrence import *

#######################初始化########################
os.chdir(sys.path[0])  # 將工作目錄設置為目前檔案所在的目錄

#######################元件指令########################


def get_video_info_gui():
    # 建立YouTube物件
    _, _, _, _, res = get_video_info(url_entry.get())
    # 將res_option的選項清空
    res_option['menu'].delete(0, 'end')
    for r in res:
        # 將res_option的選項更新為res的內容
        # command=tk._setit(res_var, r)代表選擇選項後會將res_var的值設為r
        res_option['menu'].add_command(label=r, command=tk._setit(res_var, r))

    # 預設選項為第一個選項
    res_var.set(res[0])


def download_video_gui():
    # 判斷解析度有沒有在目前的streams裡面
    if download_video(url_entry.get(), res_var.get()):
        # 更新下載完成的訊息
        download_label.config(text="下載完成")
    else:
        # 更新下載完成的訊息
        download_label.config(text="解析度錯誤")


#######################建立視窗########################

window = tk.Tk()
window.title("YT download App")

style = Style(theme="minty")

#######################建立元件########################
url_label = Label(window, text="請輸入YouTube影片網址:")
url_label.grid(row=0, column=0, padx=10, pady=10)

url_entry = Entry(window, width=50)
url_entry.grid(row=0, column=1, padx=10, pady=10)

search_button = Button(window, text="搜尋影片資訊", command=get_video_info_gui)
search_button.grid(row=0, column=2, padx=10, pady=10)

res_label = Label(window, text="請選擇影片解析度:")
res_label.grid(row=1, column=0, padx=10, pady=10)

# 建立resulation的下拉選單
res_var = tk.StringVar()
res_option = OptionMenu(window, res_var, ())
res_option.grid(row=1, column=1, padx=10, pady=10)

# 建立下載按鈕
download_button = Button(window, text="下載影片", command=download_video_gui)
download_button.grid(row=1, column=2, padx=10, pady=10)

# 下載完成的訊息
download_label = Label(window, text="")
download_label.grid(row=2, column=0, padx=10, pady=10)

#######################運行應用程式########################
window.mainloop()