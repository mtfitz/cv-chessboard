import cv2
import datetime
import time

vc = cv2.VideoCapture(0)
time.sleep(0.5)
ret, frame = vc.read()
cv2.imwrite("%s.jpg" % datetime.datetime.now(), frame)
