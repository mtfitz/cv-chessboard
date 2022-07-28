import cv2

vc = cv2.VideoCapture(0)

while True:
	ret, frame = vc.read()
	cv2.imshow("Monitor", frame)
	cv2.waitKey(int(1000 * 1.0 / 30))
