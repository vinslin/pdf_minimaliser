import cv2
import os
import numpy as np

# Function to apply CLAHE and Laplacian sharpening to an image
def enhance_image(image):
    # Apply CLAHE (Contrast Limited Adaptive Histogram Equalization)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    enhanced_image = clahe.apply(image)

    # Apply Laplacian for sharpening
    laplacian = cv2.Laplacian(enhanced_image, cv2.CV_64F)
    sharpened = cv2.convertScaleAbs(laplacian)

    # Combine the original image with the sharpened image
    processed_image = cv2.addWeighted(enhanced_image, 1.5, sharpened, -0.5, 0)

    return processed_image


def enhanced(img_list):
    enhanced=[]

    #iterate through the list of images
    for i in img_list:
        i=np.array(i)
        i= cv2.cvtColor(i,cv2.COLOR_BGR2GRAY)
        i=enhance_image(i)
        enhanced.append(i)


    return enhanced



