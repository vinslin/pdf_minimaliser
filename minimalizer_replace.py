import re

def replace_words(paragraph, left_words, right_words):
    updated_paragraph = paragraph  # Create a copy of the original paragraph to modify
    for i in range(len(left_words)):
        old_word = left_words[i]
        new_word = f"{right_words[i]}"
        # Perform case-insensitive replacement for all occurrences
        updated_paragraph = re.sub(re.escape(old_word), new_word, updated_paragraph, flags=re.IGNORECASE)

    return updated_paragraph


