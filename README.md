# Infinite-pop-ups 无限弹窗

## 环境配置

Python3.8

用到的库：tkinter（弹出窗口）、random（随机窗口位置）、threading（线程库，让多个窗口同时弹出）、time（等待秒数，避免太快导致程序没有反应时间，从而卡死）、os（用os.system函数打开CMD等软件）、playsound（播放《只因你太美》——小黑子默默露出鸡脚……）、PIL（弹表情包）

## 功能介绍

可以弹出许多颜色各异的恶搞窗口，还有CMD、计算器、记事本等软件，有《只因你太美》的背景音乐。弹一段时间后重启。

## 使用方法

使用 Pyinstaller6.6.0 进行打包，打包命令：`pyinstaller --onefile --add-data "1.png;." --add-data "ji.mp3;." main.py`

源程序是 main.py，dist/main.exe 文件可以独立运行，注意把 1.png、ji.mp3 放和 main.exe 到同一文件夹下。

请不要频繁使用，可能导致电脑性能下降（给好朋友用当然可以）。

Update: 2024.6.8 觉得CMD等软件影响效果，就注释掉了。可以手动打开。提供两种版本的exe文件。

## Environmental configuration

Python 3.8
Used libraries: tkiner (pop-up window), random (random window position), threading (thread library, allowing multiple windows to pop up at the same time), time (waiting for seconds to prevent the program from getting stuck due to not responding too quickly), os (using the os. system function to open CMD and other software), playsound (playing "Just Because You're Too Beautiful" - Little Blackie silently reveals his chicken feet...), PIL (emoticon)

## Function Introduction

Many spoof windows with different colors can pop up, as well as software such as CMD, calculator, and notepad, with background music from "Just Because You're Too Beautiful". Reboot after playing for a while.

## Usage

Use Pyinstaller6.6.0 for packaging, packaging command: ` pyinstaller -- onefile -- add data "1. png;." -- add data "ji. mp3;." main. py`
The source program is main.py, and the dist/main.exe file can be run independently. Please note to place 1.png, ji. mp3, and main.exe in the same folder.
Please do not use it frequently as it may cause a decrease in computer performance (of course, it can be used by good friends).

Update: On June 8, 2024, I commented out the impact of software such as CMD on the results. It can be manually opened. Provide two versions of the exe file.