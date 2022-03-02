import pyautogui
import cv2
#from skimage.measure import compare_ssim
import numpy as np


_screen = np.array(pyautogui.screenshot())
img = cv2.cvtColor(_screen, cv2.COLOR_RGB2GRAY)

target = cv2.imread('image/1.png', cv2.IMREAD_GRAYSCALE)

# cv2.imshow('target', target)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

result = cv2.matchTemplate(img, target, cv2.TM_CCOEFF_NORMED)
print(result)

minValue, maxValue, minLoc, maxLoc = cv2.minMaxLoc(result)
print(minValue, maxValue, minLoc, maxLoc)

leftTop = maxLoc

rightBottom = maxLoc[0]+ target.shape[1], maxLoc[1] + target.shape[0]

cv2.rectangle(_screen, leftTop, rightBottom, (255,255,0), 3)

cv2.imshow("result", _screen)
cv2.waitKey(0)
cv2.destroyAllWindows()