# OMR-Scanner
### To accomplish this, our implementation will need to satisfy the following 7 steps:

Step #1: Detect the exam in an image.

Step #2: Apply a perspective transform to extract the top-down, birds-eye-view of the exam.

Step #3: Extract the set of bubbles (i.e., the possible answer choices) from the perspective transformed exam.

Step #4: Sort the questions/bubbles into rows.

Step #5: Determine the marked (i.e., “bubbled in”) answer for each row.

Step #6: Lookup the correct answer in our answer key to determine if the user was correct in their choice.

Step #7: Repeat for all questions in the exam.

### Libraries Used:

- [argparse](https://towardsdatascience.com/learn-enough-python-to-be-useful-argparse-e482e1764e05)
- [imutils](https://github.com/PyImageSearch/imutils)
- [opencv](https://docs.opencv.org/4.x/db/deb/tutorial_display_image.html)
