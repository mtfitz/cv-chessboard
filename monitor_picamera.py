from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2

with PiCamera() as camera:
    stream = PiRGBArray(camera)
    camera.resolution = (640,480)
    camera.framerate = 30
    for frame in camera.capture_continuous(stream, format='bgr', use_video_port=True):
        image = frame.array
        cv2.imshow('Monitor', image)
        if cv2.waitKey(33) == 27:
            break
        
        stream.truncate()
        stream.seek(0)
