import time
import wmi
import cv2
import numpy as np
import matplotlib.pyplot as plt
import init
import lib
# import game
import yolo

# 회원 = game.회원정보(init.main_id, init.main_pw)
# 기본설정 = game.기본설정(회원,"")
# 환경설정 = game.환경설정(기본설정)
# print(환경설정["미니맵"])

up_list = init.os.listdir("res/roon/datas/up")
down_list = init.os.listdir("res/roon/datas/down")
right_list = init.os.listdir("res/roon/datas/right")
left_list = init.os.listdir("res/roon/datas/left")

directions = {
    "up": up_list,
    "down": down_list,
    "right": right_list,
    "left": left_list
}

while True:


    find = False

    for derection in directions:
        images = directions[derection]

        for img in images:
            print(img)
            file = "roon/datas/{}/".format(derection) + img
            if (lib.이미지찾기(file, 0.80, "20230519 140844")):
                print(derection)
                lib.키입력(eval("init.{}".format(derection)))
                time.sleep(1)
                find = True
                break

        if (find):
            break