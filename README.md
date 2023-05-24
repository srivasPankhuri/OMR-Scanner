# OMR-Scanner

The OMR Scanner is a project that aims to analyze OMR (Optical Mark Recognition) sheets at any angle and evaluate them accurately. This scanner utilizes computer vision techniques and image processing algorithms to extract and interpret the marks made on the OMR sheets, regardless of their orientation.

## Features

- **Angle Tolerance**: The OMR Scanner is capable of handling OMR sheets with various angles and orientations, ensuring accurate mark recognition and evaluation.
- **Image Processing**: The scanner applies image processing techniques such as edge detection, contour detection, and perspective transformation to preprocess the OMR sheet images and enhance mark visibility.
- **Mark Extraction**: By utilizing computer vision algorithms, the scanner accurately locates and extracts the marks made on the OMR sheets, enabling further analysis.
- **Mark Evaluation**: The extracted marks are evaluated using predefined answer keys or user-defined criteria, allowing for the calculation of scores or other relevant metrics.
## To accomplish this, our implementation will need to satisfy the following 7 steps:

Step #1: Detect the exam in an image.

Step #2: Apply a perspective transform to extract the top-down, birds-eye-view of the exam.

Step #3: Extract the set of bubbles (i.e., the possible answer choices) from the perspective transformed exam.

Step #4: Sort the questions/bubbles into rows.

Step #5: Determine the marked (i.e., “bubbled in”) answer for each row.

Step #6: Lookup the correct answer in our answer key to determine if the user was correct in their choice.

Step #7: Repeat for all questions in the exam.

## Libraries Used:

- [argparse](https://towardsdatascience.com/learn-enough-python-to-be-useful-argparse-e482e1764e05)
- [imutils](https://github.com/PyImageSearch/imutils)
- [opencv](https://docs.opencv.org/4.x/db/deb/tutorial_display_image.html)


## How to run the python file:
- Fork and Clone this repository in your local system.
  ![image](https://user-images.githubusercontent.com/84925346/224495277-33f23487-94bb-4a62-9f30-35626c5d38dd.png)
- Open the directory of the project folder in Command Prompt.
  ![image](https://user-images.githubusercontent.com/84925346/224492161-bb5c9f0b-924f-4b49-850f-e783efd9bde5.png)
- Make sure all the Libraries are installed and up-to-date.
- Type the following to determine the score of the OMR sheet in the image.png file given in this repository.
  ![image](https://user-images.githubusercontent.com/84925346/224492269-48e162d7-2032-4dce-996f-810b2056195c.png)
- If you want to test OMRs of your choice then add it in the Images folder of this repository and run the following command:
  ![image](https://user-images.githubusercontent.com/84925346/224492358-d500b83c-1053-4022-a051-3acfe45334c6.png)
  
## Contributing

Contributions are welcome! If you want to contribute to this project, please fork the repository and create a new branch. Submit any pull requests or open issues for further discussion.

## Acknowledgements

I would like to express our gratitude to the contributors and the open-source community for their valuable resources and inspiration used in building this OMR Scanner project. Their dedication and expertise have been instrumental in its development and success.
