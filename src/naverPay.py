import pyautogui
import cv2
#from skimage.measure import compare_ssim
import time
import numpy as np
import config

def naverPayAutoCheckout():
    locateArr = np.empty((0,2), float)

    _screen = np.array(pyautogui.screenshot())
    img = cv2.cvtColor(_screen, cv2.COLOR_RGB2GRAY)

    for i in config.NAVER_PAY.PASSWORD:
        target = cv2.imread(f'image/{i}.png', cv2.IMREAD_GRAYSCALE)
        result = cv2.matchTemplate(img, target, cv2.TM_CCOEFF_NORMED)

        minValue, maxValue, minLoc, maxLoc = cv2.minMaxLoc(result)

        width_center = maxLoc[0] + (target.shape[1] / 2)
        height_center = maxLoc[1] + (target.shape[0] / 2)

        locateArr = np.append(locateArr, np.array([[width_center, height_center]]), axis=0)

        #leftTop = maxLoc
        #print(minValue, maxValue, minLoc, maxLoc)
        #rightBottom = maxLoc[0]+ target.shape[1], maxLoc[1] + target.shape[0]
        #cv2.rectangle(_screen, leftTop, rightBottom, (255,255,0), 3)

    # cv2.imshow("result", _screen)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    for x in locateArr:
        print(x)
        pyautogui.moveTo(x[0], x[1])
        pyautogui.click()
        time.sleep(1)

#naverPayAutoCheckout()