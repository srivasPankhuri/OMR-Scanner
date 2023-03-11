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


### How to run the python file:
- Fork and Clone this repository in your local system.
- Open the directory of the project folder in Command Prompt.
  ![image](https://user-images.githubusercontent.com/84925346/224492161-bb5c9f0b-924f-4b49-850f-e783efd9bde5.png)
- Make sure all the Libraries are installed and up-to-date.
- Type the following to determine the score of the OMR sheet in the image.png file given in this repository.
  ![image](https://user-images.githubusercontent.com/84925346/224492269-48e162d7-2032-4dce-996f-810b2056195c.png)
- If you want to test OMRs of your choice then add it in the Images folder of this repository and run the following command:
  ![image](https://user-images.githubusercontent.com/84925346/224492358-d500b83c-1053-4022-a051-3acfe45334c6.png)

