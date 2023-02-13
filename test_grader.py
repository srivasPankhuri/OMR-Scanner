# Import Packages
from imutils.perspective import four_point_transform
from imutils import contours
import numpy as np
import argparse
import imutils
import cv2

# Construct the argument parse and parse the arguments
ap=argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True,help="path to the input image") # Created an Optional Argument , --image is the input bubble sheet test image that we are going to grade for correctness.
args=vars(ap.parse_args())

# Mapping the answer key to the Question Number:
# For question: 0 indicates 1
# For Answer: 0 indicates A
ANSWER_KEY={0:1,1:4,2:0,3:3,4:1}


### Preprocessing our input image:

# Load the image:
image=cv2.imread(args["image"])
# Convert to gray Scale:
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
# Blur the image(To reduce high frequency noise):
blurred=cv2.GaussianBlur(gray,(5,5),0)
# Find the edges:
edged=cv2.Canny(blurred,75,200)

cv2.imshow("Silhouette Image",edged)


# Finding contours in the edge map
cnts=cv2.findContours(edged.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cnts=imutils.grab_contours(cnts)
docCnt=None
# Ensure that atleast one contour is found
if len(cnts)>0:
    # Sort the contours according to their size in descending oreder
    cnts=sorted(cnts,key=cv2.contourArea,reverse=True)
    # Loop over sorted contours
    for c in cnts:
        # Approximate the contour
        peri=cv2.arcLength(c,True)
        approx=cv2.approxPloyDP(c,0.02*peri,True)

        # If our approximated contour has four points, then we assume that we have found the test sheet
        if len(approx)==4:
            docCnt=approx
            break

