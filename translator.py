from mtranslate import translate

def translate_words(words_list, target_lang):
    translated_words = []
    for word in words_list:
        translated_word = translate(word, target_lang, 'en')
        translated_words.append(translated_word)
    return translated_words
