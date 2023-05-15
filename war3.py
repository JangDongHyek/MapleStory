import time
import datas
import init
import lib
import game
import threading

# 케릭터 = "아카데미강시"
케릭터 = "장동혁100"
main = True
매크로 = True
while main :
    time.sleep(1)

    if init.win32api.GetKeyState(0x05) :
        if 매크로:
            lib.프린트("매크로시작")
            매크로 = False

        arrys1 = [(246,788),(246,803),(240,807),(246,813),(246,825),(221,826),(214,826),(188,826),(188,810),(188,805),(190,790),(213,789),(221,789)]

        for i in arrys1 :
            if not init.win32api.GetKeyState(0x05):
                exit()
            lib.키입력(init.shift,True)
            time.sleep(0.1)
            lib.키입력(init.a,True)
            time.sleep(0.1)
            lib.마우스클릭(i)
            time.sleep(0.1)
            lib.키입력(init.shift, False)
            time.sleep(0.1)
            lib.키입력(init.a, False)
            time.sleep(0.1)

            for e in range(7) :
                if not init.win32api.GetKeyState(0x05):
                    exit()

                time.sleep(1)


        lib.키입력(init.f4)


        for e in range(9):
            if not init.win32api.GetKeyState(0x05):
                exit()

            time.sleep(1)

    else :
        if not 매크로 :
            lib.프린트("매크로종료")
            매크로 = True
