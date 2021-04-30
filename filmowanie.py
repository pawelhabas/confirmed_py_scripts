import time
from datetime import datetime
import cv2
import winsound

# cam = cv2.VideoCapture(0)
cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)    # jeśli domyślna kamera lapka to 0, jeśli dodatkowa po USB to np. 1

filename = 'foto_[x].jpg' # nazwa pliku schemat 

for i in range(0, 6):
    teraz = str(datetime.now()).replace('-','').replace(' ','').replace(':','')[2:14]
    # print(teraz)
    # plik = filename.replace('[x]', str(teraz))
    plik = filename.replace('[x]', str(teraz))  # plik zgodny ze schematem "foto_datagodzina.jpg"
    ret, frame1 = cam.read()
    cv2.imwrite(plik, frame1)
    time.sleep(10) # co ile sekund nowy plik

#       Tutaj jest cześć na gdzie system odpali określony plik WAV jeśli rozpozna ruch na kamerze
#       Obecnie nie wykorzystywane
# while cam.isOpened():
#     ret, frame1 = cam.read()
#     ret, frame2 = cam.read()
#     diff = cv2.absdiff(frame1, frame2)
#     gray = cv2.cvtColor(diff, cv2.COLOR_RGB2GRAY)
#     blur = cv2.GaussianBlur(gray, (5, 5), 0)
#     _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
#     dilated = cv2.dilate(thresh, None, iterations=3)
#     contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#     # cv2.drawContours(frame1, contours, -1, (0, 255, 0), 2)
#     for c in contours:
#         if cv2.contourArea(c) < 5000:
#             continue
#         x, y, w, h = cv2.boundingRect(c)
#         cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2)
#        # winsound.PlaySound('alert.wav', winsound.SND_ASYNC)
#     if cv2.waitKey(10) == ord('q'):
#         break
#     cv2.imshow('Granny Cam', frame1)
