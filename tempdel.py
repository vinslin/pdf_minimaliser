import re

def replace_words(paragraph, left_words, right_words, printing_options):
    if printing_options == "Inttergrate_with_Paragraph":
        updated_paragraph = paragraph  # Create a copy of the original paragraph to modify
        for i in range(len(left_words)):
            old_word = left_words[i]
            new_word = f"{old_word}({right_words[i]})"
            # Perform case-insensitive replacement for the first occurrence
            if re.search(re.escape(old_word), updated_paragraph, flags=re.IGNORECASE):
                updated_paragraph = re.sub(re.escape(old_word), new_word, updated_paragraph, count=1, flags=re.IGNORECASE)
        return updated_paragraph

# Example usage
paragraph = "This is a test paragraph. Replace first occurrence of the word test."
left_words = ["test", "replace"]
right_words = ["example", "substitute"]
printing_options = "Inttergrate_with_Paragraph"

updated_paragraph = replace_words(paragraph, left_words, right_words, printing_options)
print(updated_paragraph)
