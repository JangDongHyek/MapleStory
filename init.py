import lib

import win32con
import win32gui
import win32api
import win32ui
from PIL import Image,ImageGrab

import cv2
import numpy as np
import random
import time
import platform
import subprocess
import os
import mss
import winsound
import playsound

import math
from ctypes import *
import pymysql
import pytesseract

from gtts import gTTS


# 이미지 한글추출 태서렉트 활성화
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


# DB연결
try :
    conn = pymysql.connect(host='localhost',user='maple',password='141215',db='maple',charset='utf8')
    lib.프린트("DB연결")
    cur = conn.cursor(pymysql.cursors.DictCursor)
except :
    lib.프린트("DB연결실패")

#백그라운드 (클래스,캡션)
hwnd1 = win32gui.FindWindow("MapleStoryClass",None)
# hwnd2 = win32gui.GetWindow(hwnd1, win32con.GW_CHILD)
# hwnd3 = win32gui.GetWindow(hwnd2, win32con.GW_CHILD)
hwnd = hwnd1

# 하드웨어관련 .dll파일 연결확인
dd_dll = windll.LoadLibrary('C:/Users/rando/Desktop/python/MapleStory/DD94687.64.dll')
st = dd_dll.DD_btn(0) #classdd 초기설정
if st==1:
    lib.프린트("하드웨어 연결")
else:
    lib.프린트("하드웨어 연결실패")
    exit()

# 전역변수
res = "res/"
# 하드웨어 키값
esc,f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12 = 100,101,102,103,104,105,106,107,108,109,110,111,112
q,w,e,r,t,y,u,i,o,p = 301,302,303,304,305,306,307,308,309,310
n1,n2,n3,n4,n5,n6,n7,n8,n9,n0 = 201,202,203,204,205,206,207,208,209,210
a,s,d,f,g,h,j,k,l = 401,402,403,404,405,406,407,408,409
z,x,c,v,b,n,m = 501,502,503,504,505,506,507
up,left,down,right = 709,710,711,712
shift,ctrl,alt,space,enter = 500,600,602,603,313
insert,home,pageup,delete,end,pagedown = 703,704,705,706,707,708

# 자동채팅배열
채팅= []
채팅.append([q,k,s,k,s,k])#바나나
채팅.append([d,h,f,p,s,w,l])#오렌지
채팅.append([t,n,q,k,r])#수박
채팅.append([f,p,a,h,s])#레몬
채팅.append([a,p,d,l,v,m,f])#메이플
채팅.append([e,h,o,w,l,r,h,r,l])#돼지고기
채팅.append([t,h,r,h,r,l])#소고기
채팅.append([e,k,f,v,o,d,d,l])#달팽이
채팅.append([d,h,t,j,q,k,d])#오서방
채팅.append([z,k,t,k,s,e,m,f,k])#카산드라
채팅.append([w,h,s])#존
채팅.append([s,s])  # ㄴㄴ
채팅.append([d,d])  #
채팅.append([w,n,s,g,u,d,d,k])  #
채팅.append([r,c,r,c])  #
채팅.append([w,k,d,e,h,d,g,o])  #
채팅.append([a,n,j,g,k,a])  #
채팅.append([z,z,z,z,z,z])  #
채팅.append([d,k,r,o,w,h,f,f,l,s,h])  #
채팅.append([q,k,z,m,a,l,s,w,p])  #
채팅.append([q,j,e,m,f,j,d,a,l,s])  #
채팅.append([d,k,d,l,d,p,a,r,m,f,n,x])  #
채팅.append([t,m,x,k,z,m,f,o,v,m,x,m])  # 스타크래프트
채팅.append([d,n,j,z,m,f,o,v,m,x,m])  # 워크래프트
채팅.append([e,l,t,m,z,h,e,m])  #
채팅.append([f,j,q,m,e,l,f,f,l,q,j,f,l])  #
채팅.append([f,j,q,m,d,l,s,f,h,r,m,d,l,s])  #
채팅.append([f,h,f,r,r])  #
채팅.append([z,o,t,l,s,k,d,l,x,m])  #
채팅.append([e,l,d,k,q,m,f,f,h])  #디아블로
채팅.append([r,m,f,o,s,e,m,c,p,d,l,t,m])  #그랜드체이스
채팅.append([t,m,x,l,a])  #스팀
채팅.append([d,h,q,j,d,n,j,c,l])  #오버워치
채팅.append([r,m,f,k,d,n,s,e,l,e,m])  #그라운디드
채팅.append([g,j,t,m,d,r,u,d])  #
채팅.append([r,l,a,g,p,t,n])  #
채팅.append([r,l,a,t,j,d,u,s])  #
채팅.append([g,h,d,q,h,f,k])  #
채팅.append([d,l,f,d,j,s,k])  #
채팅.append([d,k,d,l,f,r,k,r,l,t,l,f,g,e,k])  #
