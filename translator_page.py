from PIL import Image
import pytesseract
import os
from mtranslate import translate

# Specify Tesseract executable path explicitly
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Replace with your actual path

def translate_page(image_list, output_file,target_lang):
    """
    Extract text from a list of images and write the text to a file.

    Parameters:
    image_list (list): A list of paths to the images.
    output_file (str): The path to the output text file.

    Returns:
    str: The name of the output file.
target_lang    """
  
    with open(output_file, 'w', encoding='utf-8') as f:
            for i, img in enumerate(image_list):
                # Use pytesseract to extract text from the image
                text = pytesseract.image_to_string(img)
                #text = re.sub(r'(\d+)', r' \1 ', text)
                #text = re.sub(r'\s+', ' ', text).strip()
                trans_text=translate(text, target_lang, 'en')
                # Write the extracted text to the file
                f.write(f"**************** page {i+1} *****************\n")
                f.write(trans_text + "\n")
                f.write(f"****************     END    *****************\n")
    
                
    return "Process Completed and Get your TXT file"






