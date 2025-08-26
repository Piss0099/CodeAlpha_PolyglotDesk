
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


          
