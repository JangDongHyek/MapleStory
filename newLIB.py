import init


def imageYolo(name = None, scale = []) :
    net = init.cv2.dnn.readNet("mapleArrow.weights", "yolov3.cfg")
    classes = []
    arrays = []
    with open("coco.names", "r") as f:
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
                "lable": label
            }

            arrays.append(obj)

    arrays.sort(key = lambda x: x["x"])

    return arrays

def imageSearch(img,confidence = 0.85) :
    name = ""

    if not "/" in img :
        name += init.res

    if "." in img :
        name += img
    else :
        name += img + ".png"

    result = init.pyautogui.locate(name,screenshot(),confidence=confidence)

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