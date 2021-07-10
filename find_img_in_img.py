"""
Skrypt do zlokalizowania jednego obrazu w drugim

youtube.com/watch?v=vXqKniVe6P8
"""

import cv2
import numpy as np

caly_img = cv2.imread('caly.png', cv2.IMREAD_UNCHANGED)
wycinek_img = cv2.imread('wycinek.png', cv2.IMREAD_UNCHANGED)


def pokazuj(opis, ekran):
    cv2.imshow(opis, ekran)
    cv2.waitKey()
    cv2.destroyAllWindows()


# pokazuj('cały', caly_img)
#
# pokazuj('Wycinek', wycinek_img)

result = cv2.matchTemplate(caly_img, wycinek_img, cv2.TM_CCOEFF_NORMED)
# pokazuj('matchTemplate', result)

min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

print(max_loc, max_val)

w = wycinek_img.shape[1]
h = wycinek_img.shape[0]

# cv2.rectangle(caly_img, max_loc, (max_loc[0] + w, max_loc[1] + h), (0,255,255), 2)

# pokazuj("Cały z prostokątem", caly_img)

threshold = .90

yloc, xloc = np.where(result >= threshold)

# print(len(xloc))

for (x, y) in zip (xloc, yloc):
    cv2.rectangle(caly_img, (x, y), (x + w, y + h), (0, 255, 255), 2)

pokazuj("Cały z prostokątem", caly_img)
