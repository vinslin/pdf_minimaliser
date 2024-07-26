import streamlit as st
from mtranslate import translate
from supported_languages import SUPPORTED_LANGUAGES

# Streamlit App
st.title('English to Other Languages Translator')

# Input text
text = st.text_area('Enter text in English to translate:', '')

# Select target language
target_lang = st.selectbox('Select target language:', list(SUPPORTED_LANGUAGES.keys()), format_func=lambda x: SUPPORTED_LANGUAGES[x])

# Translate button
if st.button('Translate'):
    if text:
        translated_text = translate(text, target_lang, 'en')
        st.text_area('Translated text:', translated_text, height=150)
    else:
        st.error('Please enter text to translate.')
