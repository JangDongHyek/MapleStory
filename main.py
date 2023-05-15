import time
import datas
import init
import lib
import game
import threading

캐릭터 = "마카데미데몬"
기본설정 = game.기본설정("melkin","141215",캐릭터)
equipment = 0x05

main = True
매크로 = True
while main :
    if init.win32api.GetKeyState(equipment) :

        if 매크로 :
            환경설정 = game.환경설정(기본설정)
            환경설정["스레드"] = False
            환경설정["equipment"] = equipment
            포탈카운트 = 0
            룬카운트 = 0
            경뿌 = True
            lib.프린트("매크로시작")
            환경설정["event"] = threading.Event()
            threading.Thread(target=game.thread사냥,args=(환경설정,),daemon=True).start()
            매크로 = False

        lib.이미지생성()
        time.sleep(0.4)
        for image in datas.위험상황:
            if (lib.이미지찾기(image)):
                환경설정["event"].set()
                time.sleep(1)
                lib.재생("special")
                lib.이미지생성(lib.현재시간(True))
                lib.프린트("(위험상황발생) | " + image)
                lib.키입력(init.f12)
                main = False

        for image in datas.시간거탐:
            if (lib.이미지찾기(image,0.60)):
                환경설정["event"].set()
                time.sleep(1)
                lib.재생("special")
                lib.이미지생성(lib.현재시간(True))
                lib.프린트("(위험상황발생) | " + image)
                lib.키입력(init.f12)
                main = False

        # if (lib.이미지찾기("석화",.60)):
        #     lib.재생("special")
        #     lib.이미지생성(lib.현재시간(True))
        #     lib.프린트("(위험상황발생) | 석화")
        #     for i in range(5) :
        #         lib.키입력(init.left)
        #         time.sleep(0.1)
        #         lib.키입력(init.right)

        if (lib.이미지찾기("묘비")):
            lib.재생("special")
            lib.이미지생성(lib.현재시간(True))
            exit()

        for i in datas.경뿌 :
            if (lib.이미지찾기(i,.70)):
                if(경뿌) :
                    lib.재생("exp")
                    경뿌 = False

        # if(lib.픽셀서치(환경설정["미니맵"],datas.노란포탈)) :
        #     if(포탈카운트 < 1) :
        #         포탈카운트 += 1
        #         lib.재생("portal")

        if(lib.픽셀서치(환경설정["미니맵"],datas.룬)) :
            환경설정["event"].set()
            lib.재생("roon")
            game.룬찾으러가기(환경설정)
            매크로 = True

        if(환경설정["스레드"]) :
            환경설정["event"].set()
            print("스레드 에러 발생 재실행")
            매크로 = True

    else :
        if not 매크로 :
            환경설정["event"].set()
            lib.프린트("매크로종료")
            lib.키입력(init.up, False)
            lib.키입력(init.down, False)
            lib.키입력(init.left, False)
            lib.키입력(init.right, False)
            매크로 = True

