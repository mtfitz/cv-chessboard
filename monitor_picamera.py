from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2

i = 0
with PiCamera() as camera:
    camera.resolution = (480,360)
    camera.framerate = 15
    stream = PiRGBArray(camera)
    ts = time.time()
    for frame in camera.capture_continuous(stream, format='bgr', use_video_port=True):
        image = frame.array
        cv2.imshow('Monitor', image)
        i += 1
        #print(time.time())
        if cv2.waitKey(33) == 27:
            break
        
        stream.truncate()
        stream.seek(0)
        
    te = time.time()
    fps = i / (te - ts)
    print(fps)
