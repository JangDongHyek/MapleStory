import numpy as np
import cv2
import pytesseract
import newLIB as nl
import datas
import os
import time
import lib
import game
import pyautogui as pg
import init

main = True
images = ["110","120","130"]
images2 = ["110on","120on","130on"]
mouserightdown = 4
mouserightup = 8

init.dd_dll = init.windll.LoadLibrary("C:/Users/rando/Desktop/python/MapleStory/ddl/DD94687.64.dll")
st = init.dd_dll.DD_btn(0)  # classdd 초기설정
if st == 1:
    lib.프린트("하드웨어 연결")
else:
    lib.프린트("하드웨어 연결실패")
    exit()
count = 0
while main :
    time.sleep(1)
    if init.win32api.GetKeyState(0x05) :
        for item in images :
            point = nl.imageSearch(item)
            if(point) :
                pg.moveTo(point[0], point[1], duration=0.2)
                break

        if(point) :
            for i in range(10) :
                init.dd_dll.DD_btn(mouserightdown)
                init.dd_dll.DD_btn(mouserightup)
                time.sleep(0.7)

            ok = nl.imageSearch("ok")
            if (ok):
                pg.moveTo(ok[0], ok[1], duration=0.2)
                init.dd_dll.DD_btn(1)
                init.dd_dll.DD_btn(2)
                time.sleep(0.2)
                lib.키입력(init.enter)
                time.sleep(3)
                lib.키입력(init.enter)
                count = 0
            else:
                lib.재생("violetta")
                exit()

        else :
            lib.재생("violetta")
            exit()
    else :
        time.sleep(1)

# time.sleep(1)
# lib.마우스클릭((803,279))