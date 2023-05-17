import time
import wmi
import cv2
import out_lib as olib
import numpy as np
import matplotlib.pyplot as plt
import init
import lib



# 잡티제거
# img = cv2.imread('a.bmp')
# dst = cv2.fastNlMeansDenoisingColored(img,None,20,10,7,21)
# img2 = olib.blurring(dst)
# img3 = olib.createSimilarColorMap(img2)
# cv2.imwrite('all2.bmp',img3)

lib.이미지생성()