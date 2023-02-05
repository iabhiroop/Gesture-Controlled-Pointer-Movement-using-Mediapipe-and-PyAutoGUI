# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 13:08:42 2022

@author: Abhiroop
"""

import cv2 as cv
import mediapipe as mp
import pyautogui as pg



capture = cv.VideoCapture(0)
mpHands=mp.solutions.hands
hands=mpHands.Hands()
mpdraw=mp.solutions.drawing_utils
ax=ay=0
while True:
    success, img = capture.read()
    image=cv.flip(img,2)
    result=hands.process(cv.cvtColor(image,cv.COLOR_BGR2RGB))
    if result.multi_hand_landmarks:
        for handmul in result.multi_hand_landmarks:
            for idt,d in enumerate(handmul.landmark):
                h,w,wh=img.shape
                x,y=int(d.x*1920),int(d.y*1080)
                if idt==8:
                    if abs(ax - x) <= 1 and abs(ay - y) <= 1:
                        x = ax
                        y = ay
                    pg.moveTo(int(x), int(y), duration=0.01)
                    ax = x
                    ay = y
        mpdraw.draw_landmarks(img,handmul,mpHands.HAND_CONNECTIONS)
    cv.imshow("Camera", image)
    if cv.waitKey(1) & 0xFF==ord('q'):
        break


capture.release()
cv.destroyAllWindows()