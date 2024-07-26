from PIL import Image
import pytesseract
import os
import repharse_beginner_words as bw
import repharse_intermediate_words as iw
import minimalizer_replace as func

import re
#import streamlit as st

# Specify Tesseract executable path explicitly
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Replace with your actual path

def extract_text_from_images(image_list, output_file,fluency_level):
    """
    Extract text from a list of images and write the text to a file.

    Parameters:
    image_list (list): A list of paths to the images.
    output_file (str): The path to the output text file.

    Returns:
    str: The name of the output file.
    """
    if fluency_level=="Beginner":
        with open(output_file, "w") as f:
            for i, img in enumerate(image_list):
                # Use pytesseract to extract text from the image
                text = pytesseract.image_to_string(img)
                #text = re.sub(r'(\d+)', r' \1 ', text)
                #text = re.sub(r'\s+', ' ', text).strip()

                if (len(text) > 100):
                    matches_left, matches_right = bw.get_response(text)

                    updated = func.replace_words(text, matches_left, matches_right)
                else:
                    updated=text
                # Write the extracted text to the file
                f.write(f"**************** page {i+1} *****************\n")
                f.write(updated + "\n")
                f.write(f"****************     END    *****************\n")
    
    else:
        with open(output_file, "w") as f:
            for i, img in enumerate(image_list):
                # Use pytesseract to extract text from the image
                text = pytesseract.image_to_string(img)
                #text = re.sub(r'(\d+)', r' \1 ', text)
                #text = re.sub(r'\s+', ' ', text).strip()
                if (len(text) > 100):

                    matches_left, matches_right = iw.get_response(text)
                    updated = func.replace_words(text, matches_left, matches_right)
                else:
                    updated=text
                # Write the extracted text to the file
                f.write(f"**************** page {i+1} *****************\n")
                f.write(updated + "\n")
                f.write(f"****************     END    *****************\n")
    


    return "Process Completed and Get your TXT file"

