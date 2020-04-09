import imutils
from imutils import contours
from imutils.perspective import four_point_transform
import numpy as np
import cv2
import json

# Load answer key
with open('key.json') as f:
	ANSWER = json.load(f)

# Loading the image
image = cv2.imread('test.jpg')

# OPTIONAL: cropping random objects appearing in the original image
# though recommended to crop the image into only the working space
# to prevent detecting unnecessary objects
image = image[30:1420, 0:1426]
# Resizing the image
image = imutils.resize(image, height = 900)

# Transforming image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Blurring the image
blur = cv2.GaussianBlur(gray, (3, 3), 0)

# Edging the image
edge = cv2.Canny(blur, 100, 200)

# Thresholding the image
# Mess around with the thresh and max value to be able to detect
# the contours accordingly
thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)[1]

# Taking all of the contours in the image
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
qust_cnts = []

# looping through each contours
for c in cnts:
	# getting the dimension and position of each contour
	(x, y, w, h) = cv2.boundingRect(c)
	ar = w / float(h)

	# validating if they are the contours for the questions
	if w >= 20 and h >= 20 and ar >= 0.9 and ar <= 1.3:
		qust_cnts.append(c)


qust_cnts = contours.sort_contours(qust_cnts, method='top-to-bottom')[0]

correct = 0

for x, i in enumerate(np.arange(0, len(qust_cnts), 4)):
	# since we have 100 questions with 4 answers to each question
	# we are making an array from 0 to 400 with step of 4

	# sorting the contours from left to right (default arg)
	# to recognize the correct 
	cnts = contours.sort_contours(qust_cnts[i:i+4])[0]
	bubbled = None

	for z, c in enumerate(cnts):
		# making a mask of zeros for the threshold image
		mask = np.zeros(thresh.shape, dtype='uint8')

		# drawing the contours for the first 4 contours in the sorted list
		cv2.drawContours(mask, [c], -1, 255, 1)

		# applying the mask of zeros to the threshold image
		mask = cv2.bitwise_and(thresh, thresh, mask=mask)

		# count the non zero pixel
		total = cv2.countNonZero(mask)

		# since the blacked out bubble will have the max amount of non-zero
		# in order words, the least amount of zeros 
		# its index will be the choice that the user took

		if bubbled is None or total > bubbled[0]:
			# adding the index position (z variable) to the bubble to compare
			bubbled = (total, z)

	color = (0, 0, 255) # red
	k = ANSWER[str(x)] 

	if k == bubbled[1]:
		color = (0, 255, 0) # green
		correct += 1

	# draw the contour accordingly
	cv2.drawContours(image, [cnts[k]], -1, color, 2)

score = (correct / 100.0) * 100
cv2.putText(image, f"{round(score, 2)}", (10, 40), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 3)
cv2.imshow("Graded", image)
cv2.waitKey(0)
cv2.imwrite('graded.png', image)
cv2.destroyAllWindows()
