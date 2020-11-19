import cv2
import numpy as np
from mss import mss
from PIL import Image

cap = cv2.VideoCapture(0)
while True:
    _, img = cap.read()

    cv2.rectangle(img, (340,340), (360,360), (255,0,0), 1)

    colour = img[350,350]
    cv2.putText(img, str(colour), (5,20), cv2.FONT_HERSHEY_SIMPLEX, 1,(0,0,255), 2)


    if (colour[2])>180 and (colour[1])>180 and (colour[0])<80:
        cv2.putText(img, "YELLOW", (5,50), cv2.FONT_HERSHEY_SIMPLEX, 1,(0,0,255), 2)

    cv2.imshow('img', img)

    k = cv2.waitKey(30) & 0xff
    if k==27:
        break

cap.release()
