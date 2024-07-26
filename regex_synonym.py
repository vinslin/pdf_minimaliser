import re

def extract_words(text):
    # Regex pattern to match the format "**word:** description."
   # pattern_right = r':\*\*.*?[.,\n]|$'
    pattern_right = r':\*\*.*?(?=,|\n|$)'
    pattern_left= r'^\s*\d+\.\s*\*\*[\w\s-]+:\s*'
   # pattern= r'[^a-zA-Z0-9\s]'
# Search for the pattern in the text
    matches_right = re.findall(pattern_right, text, re.MULTILINE)
    matches_left = re.findall(pattern_left, text, re.MULTILINE)
    #clear=re.sub(r'[^a-zA-Z0-9\s]', '', matches_left)
    
    while len(matches_left) != len(matches_right):
        if len(matches_left) > len(matches_right):
             del matches_left[0]
        else:
             del matches_right[0]
   
    cleaned_list = []
    
    # Iterate through each string in the input list
    for input_string in matches_left:
        # Remove special characters except alphanumeric and spaces
        cleaned_string = re.sub(r'[^a-zA-Z\s-]', '', input_string)
        cleaned_string=cleaned_string.strip()
        cleaned_list.append(cleaned_string)
        
    cleaned_right = []
     # Iterate through each string in the input list
    for input_string in matches_right:
        # Remove special characters except alphanumeric and spaces
        cleaned_string = re.sub(r'[^a-zA-Z0-9\s]', '', input_string)
        cleaned_string=cleaned_string.strip()
        cleaned_right.append(cleaned_string)

    return cleaned_list,cleaned_right
   

    
    



