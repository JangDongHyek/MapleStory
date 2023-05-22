import time
import init

def dictSelect(table,dict,addQuery = "",bool = False,sort = "_id", order = "desc") :
    # bool이 True면 복수검색

    sql = "select * from {} where ".format(table)

    index = 0
    for item in dict :
        if index < 1 :
            sql += "{} = '{}'".format(item,dict[item])
        else :
            sql += " and {} = '{}'".format(item,dict[item])
        index+= 1

    sql += addQuery

    if bool :
        sql += " order by {} {}".format(sort,order)
    init.cur.execute(sql)
    result = init.cur.fetchall() if bool else init.cur.fetchone()

    return result

def 배열안객체타겟삭제(array,field,target) :
    for index in range(0, len(array)):
        data = array[index]
        if (data[field] == target):
            del array[index]
            break
def 마우스클릭(tuple = None) :
    if(tuple) :
        init.dd_dll.DD_mov(int(tuple[0]),int(tuple[1]))
        time.sleep(0.5)
    init.dd_dll.DD_btn(1)
    init.dd_dll.DD_btn(2)

def 키입력(key,bool = None,push = 0.1) :
    if(bool == None or bool == 2) :
        init.dd_dll.DD_key(key, 1)
        time.sleep(push)
        init.dd_dll.DD_key(key, 2)
    elif (bool == True) :
        init.dd_dll.DD_key(key, 1)
    elif(bool == False) :
        init.dd_dll.DD_key(key, 2)

def 현재시간(bool = False) :
    if(bool) :
        return time.strftime('%Y%m%d %H%M%S')
    else :
        return time.strftime('%Y-%m-%d_%H:%M:%S')

def 프린트(variable) :
    print(현재시간() + " | " + variable)

def 재생(file) :
    file = "sound/" + file + ".mp3"
    init.playsound.playsound(file)

def TTS생성(text) :
    tts = init.gTTS(text=text, lang='ko')
    filename = text + '.mp3'
    tts.save(filename)

def 경고음() :
    so1 = {'do': 261, 're': 293, 'mi': 329, 'pa': 349, 'sol': 391, 'ra': 440, 'si': 493}
    mel = ['do', 'mi', 'mi', 'mi', 'sol', 'sol', 're', 'pa', 'pa', 'ra', 'si', 'si']
    dur = [4, 4, 2, 4, 4, 2, 4, 4, 2, 4, 4, 2]
    mel2 = ['sol', 'do', 'ra', 'pa', 'mi', 'do', 're']
    dur2 = [1, 1, 1, 1, 1, 1, 1]
    music = zip(mel, dur)

    for melody, duration in music:
        init.sd.Beep(so1[melody], 1000 // duration)

def 시간비교(value,elapse) :
    if(time.time() - value >= elapse) :
        return True
    return False

def 픽셀서치(points, pixcels,name = 'screenshot') :
    im = init.Image.open(name + '.bmp')  # Can be many different formats.
    screen = im.load()

    main = True
    x = points[0]
    y = points[1]

    while main:
        if x == points[2] and y == points[3]:
            main = False
        if screen[x,y] in pixcels:
            return (x, y)

        if x == points[2]:
            y += 1
            x = points[0]
        x += 1
    return None

def 이미지찾기(img,threshold = .85,name = 'screenshot') :
    if "." in img :
        img = init.res + img
    else :
        img = init.res + img + ".png"
    img_rgb = init.cv2.imread(name + '.bmp')

    img_array = init.np.fromfile(img, init.np.uint8)
    template = init.cv2.imdecode(img_array, init.cv2.IMREAD_COLOR)

    res = init.cv2.matchTemplate(img_rgb, template, init.cv2.TM_CCOEFF_NORMED)

    # 임계치 이상만 배열에 저장
    loc = init.np.where(res >= threshold)

    if (loc[0].size > 0):
        x = loc[1][0]
        y = loc[0][0]

        return (x, y)
    else:
        return None

def 이미지라인(name) :
    img = init.cv2.imread(name)
    img = init.cv2.GaussianBlur(img, (3, 3), 0)
    img = init.cv2.cvtColor(img, init.cv2.COLOR_BGR2HSV)
    coefficients = (0.001, 0, 1.2)  # (h, s, v)
    img = init.cv2.transform(img, init.np.array(coefficients).reshape((1, 3)))
    scr = init.Image.fromarray(img)
    scr = scr.convert('L')
    scr.save(name)

def 이미지생성(name = 'screenshot',arryes = [], line = False) :

    # if(len(arryes)) :
    #     im = init.ImageGrab.grab((arryes[0], arryes[1], arryes[2], arryes[3]))
    # else :
    #     im = init.ImageGrab.grab()
    # im.save(name + ".bmp")

    # 백그라운드 서취
    wDC = init.win32gui.GetWindowDC(init.hwnd)
    dcObj = init.win32ui.CreateDCFromHandle(wDC)
    cDC = dcObj.CreateCompatibleDC()
    dataBitMap = init.win32ui.CreateBitmap()
    if (len(arryes)):
        dataBitMap.CreateCompatibleBitmap(dcObj, arryes[2] - arryes[0], arryes[3] - arryes[1])
    else :
        dataBitMap.CreateCompatibleBitmap(dcObj, 1920, 1080)
    cDC.SelectObject(dataBitMap)
    if(len(arryes)) :
        cDC.BitBlt((0,0), (arryes[2] - arryes[0] , arryes[3] - arryes[1] ), dcObj, (arryes[0], arryes[1]), init.win32con.SRCCOPY)
    else :
        cDC.BitBlt((0, 0), (1920, 1080), dcObj, (0, 0), init.win32con.SRCCOPY)
    dataBitMap.SaveBitmapFile(cDC, name + ".bmp")
    dcObj.DeleteDC()
    cDC.DeleteDC()
    init.win32gui.ReleaseDC(init.hwnd, wDC)
    init.win32gui.DeleteObject(dataBitMap.GetHandle())

    if(line) :
        img = init.cv2.imread(name + ".bmp")
        img = init.cv2.GaussianBlur(img, (3, 3), 0)
        img = init.cv2.cvtColor(img, init.cv2.COLOR_BGR2HSV)
        coefficients = (0.001, 0, 1.2)  # (h, s, v)
        img = init.cv2.transform(img, init.np.array(coefficients).reshape((1, 3)))
        scr = init.Image.fromarray(img)
        scr = scr.convert('L')
        scr.save(name + ".bmp")

def 아두이노키보드 (key) :
    init.ard.write(key.encode('utf-8'))
    print(key.encode('utf-8'))


def 백클릭(x,y = 0) :
    r_x = x
    r_y = y
    if (isinstance(x, tuple)):
        if (x[0] > 1920):
            r_x = x[0] - 1920
            r_y = x[1]
        else:
            r_x = x[0]
            r_y = x[1]

    init.win32gui.SendMessage(init.hwnd, init.win32con.WM_ACTIVATE, init.win32con.WA_CLICKACTIVE, 0)
    lParam = init.win32api.MAKELONG(r_x,r_y)
    init.win32gui.PostMessage(init.hwnd, init.win32con.WM_LBUTTONDOWN,init.win32con.MK_LBUTTON, lParam)
    init.win32gui.PostMessage(init.hwnd, init.win32con.WM_LBUTTONUP, init.win32con.MK_LBUTTON, lParam)