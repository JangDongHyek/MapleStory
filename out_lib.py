import init

def blurring(image, radius=10, sigmaColor=50):
    qimg = image.copy()  # 이미지 복사

    # 이미지 크기에 따라 blur 효과의 정도를 달리합니다.
    sigmaColor += (qimg.shape[1] * qimg.shape[0]) // 100000
    radius += (qimg.shape[1] * qimg.shape[0]) // 100000

    blurring = init.cv2.bilateralFilter(qimg, radius, sigmaColor, 70)

    return blurring

def createSimilarColorMap(img, value=15):
    image = img.copy()  # 이미지 복사
    map = []  # 결과 이미지 변수
    for y, row in enumerate(image):  # y 좌표
        line = []
        for x, bgr in enumerate(row):  # x 좌표
            colorChange = False  # 색 변경 여부
            blue, green, red = bgr  # 해당 좌표의 색 추출
            for c in [-1, 1]:  # 상하좌우 비교
                try:  # indexError 방지를 위해 예외 처리 구문 삽입
                    b, g, r = image[y, x + c]  # x 축 좌우 색 추출
                    # 같은 색이면 pass
                    if b == blue and g == green and r == red:
                        pass
                    # 색이 -value < color < +value 사이 값이면 색 변경
                    elif b - value < blue < b + value and \
                            g - value < green < g + value and \
                            r - value < red < r + value:
                        line.append([b, g, r])
                        image[y][x] = [b, g, r]
                        colorChange = True
                        break
                except IndexError as e:
                    pass

                try:
                    b, g, r = image[y + c, x]  # y 축 상하 색 추출
                    if b == blue and g == green and r == red:
                        pass
                    elif b - value < blue < b + value and \
                            g - value < green < g + value and \
                            r - value < red < r + value:
                        line.append([b, g, r])
                        image[y][x] = [b, g, r]
                        colorChange = True
                        break
                except IndexError as e:
                    pass
            # 만약 색 변경이 없다면, 기존 색 입력
            if not colorChange: line.append([blue, green, red])

        map.append(line)
    # numpy nd.array 형태로 반환
    return init.np.array(map)

