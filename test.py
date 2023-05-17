import time

import wmi
import pywin
import init
import lib
import game

lib.이미지생성()
time.sleep(1)
이름 = lib.이미지찾기("이름")

if(이름) :
    lib.이미지생성("캐릭터", [이름[0] + 50, 이름[1], 이름[0] + 150, 이름[1] + 15])

    접속캐릭터 = init.pytesseract.image_to_string('캐릭터.bmp', lang='kor+eng',
                                             config='-c preserve_interword_spaces=1 --psm 3')
    접속캐릭터 = init.re.sub('[\n,",;,|, ]', "", 접속캐릭터)


print(이름)
print(접속캐릭터)