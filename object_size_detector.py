# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 11:22:48 2022

@author: PLAP033
"""
import cv2
from support_file import *
import numpy as np

#height =31.4cm ratio =37.25 


# Load Object Detector
detector = HomogeneousBgDetector()

 # Load Cap
cap = cv2.VideoCapture(1)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720) 


while True:
    _, img = cap.read()
    contours = detector.detect_objects(img)
     
    # Draw objects boundaries
    for cnt in contours:
        # Get rect
        rect = cv2.minAreaRect(cnt)
        (x, y), (w, h),angle = rect
        box = cv2.boxPoints(rect)
        box = np.int0(box)
        max_ = max(h,w)
        min_ = min(h,w)
        h = max_
        w = min_
        h = h / 7.6
        w = w / 7.6
        print(h,w)
        cv2.circle(img, (int(x), int(y)), 5, (0, 0, 255), -1)
        cv2.polylines(img, [box], True, (255, 0, 0), 2)
        cv2.putText(img, "Width {} cm ".format(round(w, 1)), (int(x - 100), int(y - 20)), cv2.FONT_HERSHEY_PLAIN, 2, (100, 200, 0), 2)
        cv2.putText(img, "Height {} cm".format(round(h, 1)), (int(x - 100), int(y + 15)), cv2.FONT_HERSHEY_PLAIN, 2, (100, 200, 0), 2)
    # cv2.drawContours(img, contours, -1, (0, 255, 0), 3)
    cv2.imshow("Image", img)
    key = cv2.waitKey(1)
    if key == 27: 
        break
cap.release()
cv2.destroyAllWindows()