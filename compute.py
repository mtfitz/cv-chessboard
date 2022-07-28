import math
import cv2
import numpy as np
import glob

criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
objp = np.zeros((7*7, 3), np.float32)
objp[:,:2] = np.mgrid[0:7,0:7].T.reshape(-1,2)
objpoints = []
imgpoints = []
images = glob.glob('*.jpg')

lower_bound = np.array([0,0,143])
upper_bound = np.array([179,61,252])

img_size = None

print("Begin chessboard exercise!")

for fname in images:
	print("\nProcessing: %s" % fname)
	
	# load image, get b/w mask
	img = cv2.imread(fname)
	if img_size == None:
		gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
		img_size = gray.shape[::-1]
	hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
	mask = cv2.inRange(hsv, lower_bound, upper_bound)

	# isolate chessboard
	kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (50,30))
	dilated = cv2.dilate(mask, kernel, iterations=5)
	res = 255 - cv2.bitwise_and(dilated, mask)
	res = np.uint8(res)
	
	cv2.imshow('Chessboard', res)
	cv2.waitKey(500)
	
	print("Finding corners...")
	ret, corners = cv2.findChessboardCorners(res, (7,7), None)
	if ret == True:
		print("Success! Adjusting and displaying...")
		objpoints.append(objp)
		corners2 = cv2.cornerSubPix(res, corners, (11,11), (-1,-1), criteria)
		imgpoints.append(corners)
		cv2.drawChessboardCorners(img, (7,7), corners2, ret)
		cv2.imshow('Chessboard', img)
		cv2.waitKey(500)
	else:
		print("Something went wrong! Skipping...")

print("\nFound %d object points and %d image points." % (len(objpoints), len(imgpoints)))
ret, mat, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, img_size, cameraMatrix = None, distCoeffs = None)
print("Matrix:")
print(mat)

cv2.destroyAllWindows()
