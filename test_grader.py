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
cv2.waitKey(0)


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
        approx=cv2.approxPolyDP(c,0.02*peri,True)

        # If our approximated contour has four points, then we assume that we have found the test sheet
        if len(approx)==4:
            docCnt=approx
            break

# Apply a four point perspective transform to both the original image and grayscale image to obtain a top-down birds eye view of the paper
paper=four_point_transform(image,docCnt.reshape(4,2))
warped=four_point_transform(gray,docCnt.reshape(4,2))
cv2.imshow("Bird Eye",paper)
cv2.waitKey(0)
cv2.imshow("Bird Eye2",warped)
cv2.waitKey(0)


#Binarization
#Apply Otsu's thresholding method to binarize the warped piece of paper
thresh= cv2.threshold(warped,0,255,cv2.THRESH_BINARY_INV|cv2.THRESH_OTSU)[1]
cv2.imshow("Thresh",thresh)
cv2.waitKey(0)

#Find contours in the thresholded image, then initiaalize the list of contours that correspond to questions
cnts=cv2.findContours(thresh.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cnts=imutils.grab_contours(cnts)

questionCnts=[]

#loop over the contours
for c in cnts:
    #compute the bounding box of teh contour, then use the bounding box to derive the aspect ratio
    (x,y,w,h)=cv2.boundingRect(c)
    ar=w/float(h)
    #in order to label the contour as a question,region should be suffeciently wide, sufficiently tall, and have an aspect ratio approximately equal to 1
    if w>=20 and h>=20 and ar>=0.9 and ar<=1.1:
        questionCnts.append(c)

# Sort the question contours top-to-bottom, then initialize the total number of correct naswers
questionCnts = contours.sort_contours(questionCnts, method="top-to-bottom")[0]
correct=0

# each question has 5 possible answers, to loop over the question in batches of 5
for (q,i) in enumerate(np.arange(0,len(questionCnts),5)):
    # sort the contojurs for the current question from left to right, then initialize the index of the bubbled answer
    cnts=contours.sort_contours(questionCnts[i:i+5])[0]
    bubbled=None


    # loop over the sorted contours
    for(j,c) in  enumerate(cnts):
        #construct a mask that reveals only the current "bubble" for the question
        mask=np.zeros(thresh.shape,dtype="uint8")
        cv2.drawContours(mask,[c],-1,255,-1)

        #apply the mask to the thresholded image, then count the number of non-zeros pixels in the bubble area
        mask=cv2.bitwise_and(thresh,thresh,mask=mask)
        total=cv2.countNonZero(mask)

        #if the current total has a larger number of total non-zero pixels, then we are examining the currently bubbled-in answer
        if bubbled is None or total>bubbled[0]:
            bubbled=(total,j)


    # Initialize the contour color and the index of the "Correct" answer
    color=(0,0,255)
    k=ANSWER_KEY[q]

    # Check to see if the bubbled answer is correct
    if k==bubbled[1]:
        color=(0,255,0)
        correct+=1

    # Draw the outline of the correct answer on the test
    cv2.drawContours(paper,[cnts[k]],-1,color,3)


score=(correct/5.0)*100.0
print("[INFO] score: {:.2f}%".format(score))
cv2.putText(paper,"{:.2f}%".format(score),(10,30), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0,0,255),2)
cv2.imshow("ORIGINAL",image)
cv2.imshow("EXAM",paper)
cv2.waitKey(0)