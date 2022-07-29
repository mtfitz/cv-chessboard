import cv2

vc = cv2.VideoCapture(0)

while True:
	ret, frame = vc.read()
	frame = cv2.resize(frame, dsize=None, fx=0.25, fy=0.25)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
	cv2.imshow("Monitor", frame)
	if cv2.waitKey(int(1000 * 1.0 / 30)) == 27:
		break
