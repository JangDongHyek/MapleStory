import time

import cv2.dnn

import init
import lib
import datas


def 채널이동(환경설정) :
    count = 0
    main = True
    while main :
        lib.키입력(init.esc)
        time.sleep(0.5)
        lib.이미지생성()
        time.sleep(0.5)
        채널변경 = lib.이미지찾기("채널변경")
        if(채널변경) :
            lib.키입력(init.enter)
            time.sleep(1)
            lib.키입력(init.right)
            time.sleep(5)
            lib.키입력(init.enter)
            lib.프린트("채널이동")
            time.sleep(5)
            lib.이미지생성()
            time.sleep(1)
            유저 = lib.픽셀서치(환경설정["미니맵"], datas.유저)
            if (유저):
                print(유저)
                lib.프린트("유저있음 다시 채널이동")
            else :
                lib.프린트("유저없음 채널이동 완료")
                main = False
        time.sleep(1)

def 룬먹기() :
    lib.키입력(init.right, False)
    lib.키입력(init.left, False)
    lib.키입력(init.down, False)
    lib.키입력(init.up, False)
    init.time.sleep(0.5)
    lib.키입력(init.space)
    time.sleep(0.5)
    lib.이미지생성("res/roon/" + lib.현재시간(True), [690, 170, 1230, 350])
    time.sleep(0.5)

    main = True
    endx = 750

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

    while main:
        lib.이미지생성("roon", [690, 170, endx, 350])

        find = False

        for derection in directions:
            images = directions[derection]

            for img in images:
                file = "roon/datas/{}/".format(derection) + img
                if (lib.이미지찾기(file, 0.80, "roon")):
                    print(derection)
                    lib.키입력(eval("init.{}".format(derection)))
                    time.sleep(1)
                    find = True
                    break

            if (find):
                break

        if (endx > 1230):
            lib.프린트("1.5초후 룬매크로 종료")
            time.sleep(1.5)
            main = False
            break

        endx += 30

def 룬찾으러가기(환경설정) :
    main = True

    while main:

        if not init.win32api.GetKeyState(환경설정['equipment']):
            main = False

        lib.이미지생성("roon")
        위치 = lib.픽셀서치(환경설정["미니맵"],datas.룬,"roon")
        if (위치):
            케릭터위치 = lib.픽셀서치(환경설정["미니맵"], datas.내케릭터,"roon")
            # x축
            if (위치 == None or abs(위치[0] - 케릭터위치[0]) < 7):
                print("x ok")
                lib.키입력(init.right, False)
                lib.키입력(init.left, False)
                lib.키입력(init.down, False)
                lib.키입력(init.up, False)
                init.time.sleep(0.5)

                if (위치 == None or abs(위치[1] - 케릭터위치[1]) < 7):
                    print("y ok")
                    룬먹기()
                    main = False


                elif (위치[1] < 케릭터위치[1]):
                    for item in 환경설정['이동패턴']:
                        if (item['이름'] == "위"):
                            for move in item["패턴"]:
                                lib.키입력(move[0], move[1])
                                if (move[2]):
                                    init.time.sleep(move[2])
                    init.time.sleep(1)
                elif (위치[1] > 케릭터위치[1]):
                    lib.키입력(init.down, True)
                    init.time.sleep(0.1)
                    lib.키입력(init.alt, None)
                    lib.키입력(init.down, False)
                    init.time.sleep(1)

            elif (위치[0] < 케릭터위치[0]):
                lib.키입력(init.right, False)
                lib.키입력(init.left, True)
            elif (위치[0] > 케릭터위치[0]):
                lib.키입력(init.left, False)
                lib.키입력(init.right, True)

        else :
            print("위치 안읽힘")
            룬먹기()
            main = False


def thread사냥(환경설정) :
    lib.프린트('미니맵 크기 : {} {} ~ {} {}'.format(환경설정["미니맵"][0],환경설정["미니맵"][1],환경설정["미니맵"][2],환경설정["미니맵"][3]))
    lib.프린트("x축이동패턴 : " + str(환경설정["x"]))
    lib.프린트("y축이동패턴 : " + str(환경설정["y"]))
    lib.프린트("매크로 시작합니다.")
    사냥이미지 = "hunt"
    랜덤패턴시간 = init.time.time()
    try :
        while not 환경설정["event"].is_set():
            lib.이미지생성(사냥이미지)

            케릭터위치 = lib.픽셀서치(환경설정["미니맵"], datas.내케릭터, 사냥이미지)

            이동패턴 = 환경설정["이동패턴"].copy()

            # 현재 케릭터위치에 따른 x이동패턴 수정
            if (환경설정["미니맵중앙"] < 케릭터위치[0]):
                for i in range(환경설정["x"]):
                    lib.배열안객체타겟삭제(이동패턴,"이름","오른쪽")
            else:
                for i in range(환경설정["x"]):
                    lib.배열안객체타겟삭제(이동패턴,"이름","왼쪽")

            if (환경설정["미니맵y중앙"] < 케릭터위치[1]):
                for i in range(환경설정["y"]):
                    lib.배열안객체타겟삭제(이동패턴,"이름","아래")
            else:
                for i in range(환경설정["y"]):
                    lib.배열안객체타겟삭제(이동패턴,"이름","위")

            init.random.shuffle(이동패턴)

            if(lib.시간비교(랜덤패턴시간,init.random.randrange(180,240))) :
                랜덤채팅 = init.채팅[init.random.randrange(0,len(init.채팅))]
                lib.키입력(init.enter)
                init.time.sleep(init.random.uniform(0.1, 0.15))
                for item in 랜덤채팅:
                    lib.키입력(item)
                    init.time.sleep(init.random.uniform(0.03, 0.15))
                lib.키입력(init.enter)
                init.time.sleep(init.random.uniform(0.1, 0.15))
                lib.키입력(init.enter)
                랜덤패턴시간 = init.time.time()

            for 이동 in 이동패턴:
                if (환경설정["event"].is_set()):
                    break

                for item in 이동["패턴"]:
                    if (환경설정["event"].is_set()):
                        break

                    lib.키입력(item[0], item[1])
                    if (item[2]):
                        init.time.sleep(item[2])

                for 스킬 in 환경설정["스킬패턴"]:
                    if (환경설정["event"].is_set()):
                        break

                    if (lib.시간비교(스킬['time'], 스킬['cooldown'])):
                        init.time.sleep(스킬['before'])
                        lib.키입력(스킬['key'],None,스킬['keydown'])
                        스킬['time'] = init.time.time()
                        init.time.sleep(스킬['after'])


                        for 연계 in 스킬["relations"] :
                            if (lib.시간비교(연계['time'], 연계['cooldown'])):
                                init.time.sleep(연계['before'])
                                lib.키입력(연계['key'],None,연계['keydown'])
                                연계['time'] = init.time.time()
                                init.time.sleep(연계['after'])

                        break

                init.time.sleep(init.random.uniform(0.1, 0.2))
    except :
        환경설정["스레드"] = True

def 환경설정(기본설정) :
    lib.이미지생성()
    # 미니맵 크기
    for image in datas.미니맵x :
        x = lib.이미지찾기(image)  # + 40
        if(x) :
            break

    for image in datas.미니맵y :
        y = lib.이미지찾기(image)  # + 40
        if(y) :
            break
    # print(x)
    # print(y)
    if (x == None or y == None):
        lib.프린트("미니맵 크기 확인 불가")
        exit()
    미니맵 = [10, 22, x[0], y[1]]
    미니맵중앙 = ( (미니맵[2] - 8) / 1.9)
    미니맵y중앙 = (미니맵[3] / 1.7)

    # 미니맵 크기에 따른 이동반경
    if 기본설정['이동타입'] == "텔포":
        x = init.math.floor(미니맵[2] / 35)
    else :
        x = init.math.floor(미니맵[2] / 55)

    y = init.math.floor((미니맵[3] / 60))

    # 이동패턴 설정
    a = (기본설정["이동"][0], x)
    b = (기본설정["이동"][1], x)
    c = (기본설정["이동"][2], y)
    d = (기본설정["이동"][3], y)
    arrays = [a, b, c, d]
    이동패턴 = []
    for item in arrays:
        for i in range(item[1]):
            이동패턴.append(item[0])

    obj = {
        "미니맵" : 미니맵,
        "미니맵중앙" : 미니맵중앙,
        "미니맵y중앙" : 미니맵y중앙,
        "스킬패턴" : 기본설정["스킬"],
        "이동패턴" : 이동패턴,
        "x" : x,
        "y" : y,
    }

    return obj


def 회원정보(id,pw) :
    dict = {
        "id": id,
        "pw": pw
    }
    회원 = lib.dictSelect("users", dict)
    if (회원):
        lib.프린트("환영합니다 {}님".format(회원['name']))
    else:
        lib.프린트("가입된 회원이 아닙니다.")
        exit()

    lib.프린트("기기 확인중.")

    equipment = init.wmi.WMI()
    SerialNumber = ""
    for item in equipment.win32_OperatingSystem():
        SerialNumber = item.SerialNumber

    dict = {
        "u_id" : 회원['_id'],
        "SerialNumber" : SerialNumber
    }
    기기 = lib.dictSelect("equipment", dict)

    if(기기) :
        lib.프린트("{} 등록된 기기 입니다.".format(기기['CSName']))

        # 하드웨어관련 .dll파일 연결확인
        init.dd_dll = init.windll.LoadLibrary(기기['dll'])

        st = init.dd_dll.DD_btn(0)  # classdd 초기설정
        if st == 1:
            lib.프린트("하드웨어 연결")
        else:
            lib.프린트("하드웨어 연결실패")
            exit()

        if(기기['type'] == "Desk") :
            회원['equipment'] = 0x05

        else :
            회원['equipment'] = 0x02
    else :
        lib.프린트("등록된 기기가 없습니다..")


        exit()

    return 회원

def 기본설정(회원,캐릭터) :
    if 캐릭터 :
        접속캐릭터 = 캐릭터
    else :
        lib.키입력(init.s)
        time.sleep(0.5)
        lib.이미지생성()
        time.sleep(0.5)
        이름 = lib.이미지찾기("이름")
        if (이름):
            lib.이미지생성("캐릭터", [이름[0] + 55, 이름[1], 이름[0] + 150, 이름[1] + 15])
            image = init.Image.open("캐릭터.bmp")
            img_resize = image.resize((int(image.width * 3), int(image.height * 3)))
            img_resize.save("캐릭터.bmp")
            접속캐릭터 = init.pytesseract.image_to_string('캐릭터.bmp', lang='kor+eng',
                                                     config='-c preserve_interword_spaces=1 --psm 4')
            접속캐릭터 = init.re.sub('[\n,",;,|, ]', "", 접속캐릭터)

    lib.프린트("인식된 닉네임 {}".format(접속캐릭터))
    lib.키입력(init.s)

    dict = {
        "name": 접속캐릭터
    }
    닉네임 = lib.dictSelect("nickname", dict)
    if (not 닉네임):
        lib.프린트("닉네임 데이터가 존재하지 않습니다.")
        exit()

    dict = {
        "_id": 닉네임['c_id'],
        "u_id" : 회원['_id']
    }

    캐릭터 = lib.dictSelect("characters", dict)
    if 캐릭터 :
        lib.프린트("이름 : {} | 직업 : {}".format(캐릭터['name'], 캐릭터['job']))
    else :
        lib.프린트("캐릭터 데이터가 존재하지 않습니다.")
        exit()

    dict = {
        "c_id": 캐릭터['_id']
    }

    스킬 = lib.dictSelect("skills", dict," or c_id = 0", True,"cooldown","desc")
    스킬셋팅 = []
    if(스킬) :
        lib.프린트("설정된 스킬셋 {}개 불러오는중.".format(len(스킬)))

        # 스킬가공
        for skill in 스킬 :
            skill["key"] = eval("init.{}".format(skill['key']))
            skill["time"] = eval(skill['time'])
            skill["relations_id"] = init.json.loads(skill["relations_id"])
            skill["relations"] = init.json.loads(skill["relations"])

        # 스킬 셋팅
        for skill in 스킬 :
            if not skill['relation'] :
                for _id in skill['relations_id'] :
                    for relation in 스킬 :
                        if _id == relation['_id'] :
                            skill['relations'].append(relation)
                스킬셋팅.append(skill)

    else :
        lib.프린트("설정된 스킬셋이 없습니다.")
        exit()

    dict = {
        "type": 캐릭터['move'],
    }
    이동 = lib.dictSelect("moves",dict,"",True,"orders","asc")
    if(이동) :
        이동셋팅 = set이동패턴(이동)

    else :
        lib.프린트("설정된 이동셋이 없습니다.")
        exit()

    obj = {
        "스킬" : 스킬셋팅,
        "이동" : 이동셋팅,
        "이동타입" : 캐릭터['move']
    }
    return obj

def set이동패턴(이동) :
    왼쪽 = {
        "이름" : "왼쪽",
        "패턴" : []
    }
    오른쪽 = {
        "이름": "오른쪽",
        "패턴": []
    }
    위 = {
        "이름": "위",
        "패턴": []
    }
    아래 = {
        "이름": "아래",
        "패턴": []
    }
    for item in 이동 :
        data = (eval("init.{}".format(item['key'])), item['keydown'],item['delay'])

        eval(item['direction'])["패턴"].append(data)

    return 왼쪽,오른쪽,위,아래