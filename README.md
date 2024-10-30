### Image Classification for a City Dog Show - README
## Project Overview
This project aims to classify images submitted during a city dog show registration process. The goal is to determine if the submitted images are of dogs, and if so, to identify the breed using pre-trained Convolutional Neural Networks (CNNs). Three different CNN architectures (ResNet, AlexNet, VGG) will be tested to determine which model performs best in terms of accuracy and runtime.

## Files in the Project
The following files are included in this project:

check_images.py: The main Python script that runs the program. It handles command-line arguments, processes images, classifies them, and prints results.
classifier.py: Contains the classifier function that uses CNN models (ResNet, AlexNet, VGG) to classify images.
dognames.txt: A text file containing the names of all recognized dog breeds. This file is used to distinguish dog breeds from non-dog images.
pet_images/: A directory containing the images that will be classified.
README.md: This file, explaining the project and how to run it.

## Requirements
The project requires the following Python libraries:

Python 3.x
argparse
os
time
Pre-trained CNN models (ResNet, AlexNet, VGG) provided by classifier.py
Make sure these libraries are installed before running the project.

## How to Run the Project
# To run the project, follow these steps:

Running the Program via Command Line

Use the command below to run the program. It processes the images in the pet_images/ directory and classifies them using the selected CNN model.

bash
Kodu kopyala
python check_images.py --dir pet_images/ --model vgg --dogfile dognames.txt
--dir: The directory containing the images to be classified (default: pet_images/).
--model: The CNN model to use (resnet, alexnet, or vgg).
--dogfile: The path to the file containing dog breed names (default: dognames.txt).
Output of the Program

# The program outputs the following information:

Whether each image is classified as a dog or not.
If the image is of a dog, it provides the predicted breed.
Accuracy and performance metrics for the selected model.
A comparison of accuracy and runtime for all three CNN models.
Submitting the Project

# Once the project is complete, bundle the following files in a ZIP archive for submission:

check_images.py: The main classification code.
classifier.py: The script containing the CNN classification function.
dognames.txt: The file containing the names of recognized dog breeds.
README.md: This documentation file explaining the project and how to run it.
IMPORTANT: Do not include any image files or data in the submission archive.

## Program Workflow
Command Line Arguments: The program starts by receiving user inputs for the image directory, the CNN model to use, and the dog breed file via argparse.
Creating Pet Labels: The program processes image filenames to create pet labels (breeds) from the file names.
Classifying Images: The CNN model is used to classify each image.
Classifying as "Dog" or "Not Dog": The program checks whether each classified label corresponds to a dog using the dognames.txt file.
Calculating Results: It calculates the accuracy and other performance metrics.
Timing: The program calculates the runtime for each CNN model and reports the time taken to classify all images.
Testing the Project
The project has been tested using the provided pet images. The accuracy and runtime for each CNN model (ResNet, AlexNet, VGG) have been recorded, and the results are compared to determine the best performing model for classifying dog breeds.

## Author
This project was developed as part of the AWS AI/ML program under the "Create Your Own Image Classifier" assignment.

