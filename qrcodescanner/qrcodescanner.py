import cv2
from pyzbar.pyzbar import decode
import time

cam = cv2.VideoCapture(0)
cam.set(3, 340)
cam.set(4, 280)
camera = True
while camera ==True:
    suceess, frame = cam.read()
    for i in decode(frame):
        print(i.type)
        print(i.data.decode('utf-8'))
        time.sleep(10)
        cv2.imshow("QR_Scanner", frame)
        cv2.waitKey(3)
