import init

def pixcelPartSearch(lower,upper,name = None,save = False) :
    #특정 픽셀 서치 검색 RGB순서가아닌 BGR 순서로 값을 넣어줘야한다

    if(name) :
        img_color = init.cv2.imread(name)  # 이미지 파일을 컬러로 불러옴
    else :
        img_color = screenshot()
        img_color = init.np.array(img_color)
        img_color = init.cv2.cvtColor(img_color, init.cv2.COLOR_BGR2RGB)

    img_hsv = init.cv2.cvtColor(img_color, init.cv2.COLOR_BGR2HSV)  # cvtColor 함수를 이용하여 hsv 색공간으로 변환

    img_mask = init.cv2.inRange(img_hsv, lower, upper)  # 범위내의 픽셀들은 흰색, 나머지 검은색

    if(name) :
        names = name.split(".")
        init.cv2.imwrite(names[0] + "_part." + names[1], img_mask)  # imgs 폴더에 Lenna_GrayScale.png 이미지 저장
    else :
        if save :
            init.cv2.imwrite("pixcelPartSearch.bmp", img_mask)
        else :
            return init.Image.fromarray(img_mask)

    return None

def pixelSearch(points, pixcels) :
    screen = screenshot().load()

    main = True
    x = points[0]
    y = points[1]

    while main:
        if x == points[2] and y == points[3]:
            main = False
        if screen[x, y] in pixcels:
            return (x, y)

        if x == points[2]:
            y += 1
            x = points[0]
        x += 1
    return None

def imageYolo(weights,name = None, scale = []) :
    net = init.cv2.dnn.readNet("yolo/" + weights + ".weights","yolo/" + weights + ".cfg")
    classes = []
    arrays = []
    with open("yolo/" + weights + ".names", "r") as f:
        classes = [line.strip() for line in f.readlines()]
    layer_names = net.getLayerNames()
    output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]
    colors = init.np.random.uniform(0, 255, size=(len(classes), 4))

    # 이미지 가져오기
    if name :
        img = init.cv2.imread(name)
    else :
        if(len(scale)) :
            screen = screenshot(name,scale)
        else :
            screen = screenshot()

        img = init.np.array(screen)
        img = init.cv2.cvtColor(img, init.cv2.COLOR_BGR2RGB)

    height, width, channels = img.shape

    # Detecting objects
    blob = init.cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
    net.setInput(blob)
    outs = net.forward(output_layers)

    class_ids = []
    confidences = []
    boxes = []
    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = init.np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.5:
                # Object detected
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)
                # 좌표
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)
                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)

    indexes = init.cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

    font = init.cv2.FONT_HERSHEY_PLAIN
    for i in range(len(boxes)):
        if i in indexes:
            x, y, w, h = boxes[i]
            label = str(classes[class_ids[i]])
            color = colors[class_ids[i]]
            init.cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
            init.cv2.putText(img, label, (x, y + 30), font, 3, color, 3)

            obj = {
                "x": x,
                "y": y,
                "label": label
            }

            arrays.append(obj)

    arrays.sort(key = lambda x: x["x"])

    return arrays

def imageLine(name) :
    img = init.cv2.imread(name)
    img = init.cv2.GaussianBlur(img, (3, 3), 0)
    img = init.cv2.cvtColor(img, init.cv2.COLOR_BGR2HSV)
    coefficients = (0.001, 0, 1.2)  # (h, s, v)
    img = init.cv2.transform(img, init.np.array(coefficients).reshape((1, 3)))
    scr = init.Image.fromarray(img)
    scr = scr.convert('L')

    names = name.split(".")
    scr.save(names[0] + "_line." + names[1])

def imageSearch(img,confidence = 0.85,image = None) :
    name = ""

    if not "/" in img :
        name += init.res

    if "." in img :
        name += img
    else :
        name += img + ".png"

    # 한글이름 이미지 읽게하기
    img_array = init.np.fromfile(name, init.np.uint8)
    template = init.cv2.imdecode(img_array, init.cv2.IMREAD_COLOR)

    if image :
        result = init.pyautogui.locate(template, image, confidence=confidence)
    else :
        result = init.pyautogui.locate(template,screenshot(),confidence=confidence)

    return result

def screenshot(name = None,scale = []):
    if init.className:
        hwnd = init.win32gui.FindWindow(init.className,None)
        if hwnd:
            init.win32gui.SetForegroundWindow(hwnd)
            x, y, x1, y1 = init.win32gui.GetClientRect(hwnd)
            x, y = init.win32gui.ClientToScreen(hwnd, (x, y))
            x1, y1 = init.win32gui.ClientToScreen(hwnd, (x1 - x, y1 - y))
            if(len(scale)) :
                im = init.pyautogui.screenshot(region=(scale[0], scale[1], scale[2] - scale[0] , scale[3] - scale[1]))
            else :
                im = init.pyautogui.screenshot(region=(x, y, x1, y1))

            if name :
                im.save(name + ".bmp")

            return im
        else:
            print('Window not found!')
    else:
        im = init.pyautogui.screenshot()
        if name:
            im.save(name)
        return im

def getTime(bool = False) :
    if(bool) :
        return init.time.strftime('%Y%m%d %H%M%S')
    else :
        return init.time.strftime('%Y-%m-%d_%H:%M:%S')