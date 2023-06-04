import numpy as np
import cv2
import pytesseract
import newLIB as nl
import datas
import os
import time
import lib

# nl.screenshot("asd.bmp")
# asd = nl.pixcelPartSearch((19,178,152),(24,255,255),"c3.bmp",True)
# print(nl.screenshot())
# print(asd)
os.rename("pixcelPartSearch.bmp",lib.현재시간(True) + ".bmp")
# for img in datas.시간거탐 :
#     asd = nl.imageSearch(img,0.7,"a_part.bmp")
#     print(asd)
# aa = time.time()
# roon = nl.imageYolo("lie","c3_part.bmp")
# for file in os.listdir("click_lie") :
#     nl.pixcelPartSearch(datas.거탐색범위[0],datas.거탐색범위[1],"click_lie/"+file,True)

