"""
How to find image on your screen, locate it and click
Jak znaleść na ekranie interesujący nas obrazek i kliknięcie w niego
"""

import pyautogui
import numpy as np
import cv2

myScreenshot = pyautogui.screenshot()
# myScreenshot.save(r'Path to save screenshot\file name.png')
myScreenshot.save(r'screen.png')


def pokazuj(opis, ekran):
    cv2.imshow(opis, ekran)
    cv2.waitKey()
    cv2.destroyAllWindows()


caly_img = cv2.imread('screen.png', cv2.IMREAD_UNCHANGED)

# pokazuj('Pulpit', pulpit_img)

wycinek_img = cv2.imread('chrome.png', cv2.IMREAD_UNCHANGED)

w = wycinek_img.shape[1]
h = wycinek_img.shape[0]

result = cv2.matchTemplate(caly_img, wycinek_img, cv2.TM_CCOEFF_NORMED)

threshold = .90

yloc, xloc = np.where(result >= threshold)

# print(len(xloc))

min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
# cv2.rectangle(caly_img, max_loc, (max_loc[0] + w, max_loc[1] + h), (0,255,255), 2)

pyautogui.moveTo(max_loc[0] + w / 2, max_loc[1] + h / 2)
pyautogui.click()

# for (x, y) in zip(xloc, yloc):
#     cv2.rectangle(caly_img, (x, y), (x + w, y + h), (0, 255, 255), 2)

# pokazuj("Cały z prostokątem", caly_img)
