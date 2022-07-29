from picamera import PiCamera
from picamera.array import PiRGBArray
import cv2
import datetime
import time

with PiCamera() as camera:
    camera.resolution = (640,480)
    time.sleep(0.1)
    raw_cap = PiRGBArray(camera)
    camera.capture(raw_cap, 'bgr')
    frame = raw_cap.array
    cv2.imwrite("%s.jpg" % datetime.datetime.now(), frame)
