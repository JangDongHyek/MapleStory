import time

import init
import lib

#
#
#
main = True
매크로 = True

images = ["한번","사용하기"]
while main :
    lib.이미지생성()

    for image in images :
        이미지 = lib.이미지찾기(image)

        if(이미지) :
            lib.마우스클릭()

            lib.키입력(init.enter)
            lib.키입력(init.enter)
            lib.키입력(init.enter)
            lib.키입력(init.enter)



            time.sleep(2)



