
# PolyglotDesk: Instant Language Translator
# Author: Ravi Choudhary
# Internship: CodeAlpha AI Internship (2025)

import streamlit as st
from googletrans import Translator

# Set up Streamlit app
st.set_page_config(page_title="PolyglotDesk: Instant Translator")
st.title("🌏 PolyglotDesk")
st.write("Translate text instantly between popular languages.")

# Supported languages
languages = ['english', 'french', 'hindi', 'german', 'spanish']
lang_codes = {'english': 'en', 'french': 'fr', 'hindi': 'hi', 'german': 'de', 'spanish': 'es'}

# Inputs
src_lang = st.selectbox('Source Language', languages)
tgt_lang = st.selectbox('Target Language', languages)
input_text = st.text_area('Enter text to translate')

if st.button("Translate"):
    if not input_text.strip():
        st.warning("⚠️ Please enter some text to translate.")
    else:
        try:
            translator = Translator()
            result = translator.translate(input_text, src=lang_codes[src_lang], dest=lang_codes[tgt_lang])
            st.success(result.text)
        except Exception as e:
            st.error(f"❌ Translation failed. Possible issues: internet connection, API limit. Details: {e}")
          
