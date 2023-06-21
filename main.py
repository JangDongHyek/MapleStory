import time
import datas
import init
import lib
import newLIB as nl
import game
import threading

회원 = game.회원정보(init.main_id, init.main_pw)
equipment = 회원['equipment']

룬시간 = None
main = True
매크로 = True
logCount = 0
사냥시간 = time.time()
timer = time.time()

timer_time = 36000
lie_count = 0
while main :
    if init.win32api.GetKeyState(equipment) :

        if 매크로 :
            캐릭터 = ""
            기본설정 = game.기본설정(회원, 캐릭터)
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

        # 100초동안 이미지 로그 생성
        nl.screenshot("imageLog/{}".format(logCount))

        logCount += 1
        if(logCount > 100) :
            logCount = 0

        time.sleep(0.25)
        for image in datas.위험상황:
            if (nl.imageSearch(image)):
                환경설정["event"].set()
                time.sleep(1)
                lib.키보드해제()
                lib.재생("violetta")
                lib.키입력(init.f12)
                main = False

        # 거탐 픽셀 이미지화
        nl.pixcelPartSearch(datas.거탐색범위[0], datas.거탐색범위[1],None,True)
        if(nl.imageYolo("lie","pixcelPartSearch.bmp")) :
            lie_count += 1
            if (lie_count > 1):
                lib.재생("real_detection")
                # 서취된 파일 저장
                init.os.rename("pixcelPartSearch.bmp", lib.현재시간(True) + ".bmp")
        else :
            lie_count = 0


        if (nl.imageSearch("묘비")):
            lib.재생("special")
            nl.screenshot(lib.현재시간(True))
            exit()

        for i in datas.경뿌 :
            if (nl.imageSearch(i,.70)):
                if(경뿌) :
                    # lib.재생("exp")
                    경뿌 = False

        # if(lib.픽셀서치(환경설정["미니맵"],datas.노란포탈)) :
        #     if(포탈카운트 < 1) :
        #         포탈카운트 += 1
        #         lib.재생("portal")

        if(lib.시간비교(사냥시간,1800)) :
            환경설정["event"].set()
            time.sleep(1)
            lib.프린트("사냥한지 30분 지나서 서버이동")
            lib.키보드해제()
            game.채널이동(환경설정)
            사냥시간 = time.time()
            매크로 = True

        if (lib.시간비교(timer,timer_time)):
            환경설정["event"].set()
            lib.프린트("타이머 시간 도달 매크로 종료")
            lib.키보드해제()
            lib.키입력(init.f12)
            main = False


        if(nl.pixelSearch(환경설정["미니맵"],datas.룬)) :
            환경설정["event"].set()
            # lib.재생("roon")
            if(not 룬시간 or lib.시간비교(룬시간,30)) :
                룬시간 = time.time()
                game.룬찾으러가기(환경설정)
            else :
                game.채널이동(환경설정)

            매크로 = True

        if (nl.pixelSearch(datas.HP, datas.피없음)):
            lib.키입력(init.f11)
            lib.프린트("물약")


        if(환경설정["스레드"]) :
            환경설정["event"].set()
            print("스레드 에러 발생 재실행")
            매크로 = True

    else :
        if not 매크로 :
            logCount = 0
            환경설정["event"].set()
            lib.프린트("매크로종료")
            lib.키입력(init.up, False)
            lib.키입력(init.down, False)
            lib.키입력(init.left, False)
            lib.키입력(init.right, False)
            매크로 = True

