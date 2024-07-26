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

    else:
        result = paragraph + "\n\n"
        for i in range(len(left_words)):
            old_word = left_words[i]
            new_word = f"{old_word} = {right_words[i]}"
            result += new_word + " , "
        # Remove the trailing comma and space
        result = result.rstrip(", ")
        return result

