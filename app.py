import streamlit as st
from googletrans import Translator, LANGUAGES

# Initialize translator
translator = Translator()

# Custom CSS for animated background and enhanced UI
st.markdown("""
    <style>
    @keyframes gradientBG {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    .stApp {
        background: linear-gradient(45deg, #2a2a72, #009ffd);
        background-size: 200% 200%;
        animation: gradientBG 10s ease infinite;
    }

    .header {
        text-align: center;
        color: #ffffff;
        font-family: 'Courier New', Courier, monospace;
        font-size: 42px;
        font-weight: bold;
        margin-bottom: 10px;
        text-shadow: 2px 2px 4px #000000;
    }

    .subheader {
        color: #ffffff;
        font-family: 'Courier New', Courier, monospace;
        font-size: 20px;
        margin-bottom: 30px;
        text-shadow: 1px 1px 2px #000000;
    }

    .footer {
        text-align: center;
        margin-top: 50px;
        color: #ffffff;
        font-size: 14px;
        font-style: italic;
    }

    .result-box {
        background-color: #ffffff;
        padding: 15px;
        border-radius: 10px;
        margin-top: 20px;
        color: #333333;
        font-family: 'Verdana', sans-serif;
        font-size: 16px;
        box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.2);
    }

    .stButton button {
        background-color: #4CAF50 !important;
        color: white !important;
        font-size: 18px !important;
        padding: 10px 20px !important;
        border-radius: 5px !important;
        box-shadow: 2px 2px 8px rgba(0, 0, 0, 0.2);
        font-family: 'Courier New', Courier, monospace;
    }
    
    .stTextInput input {
        background-color: #f0f0f0 !important;
        color: #333333 !important;
        border: 1px solid #ccc !important;
        border-radius: 5px !important;
        font-size: 16px !important;
        padding: 10px !important;
        font-family: 'Verdana', sans-serif;
    }

    .stSelectbox div {
        background-color: #ffffff !important;
        border-radius: 5px !important;
        padding: 10px !important;
        font-family: 'Verdana', sans-serif;
        color: #333333 !important;
    }
    </style>
    """, unsafe_allow_html=True)

# Application Title
st.markdown('<h1 class="header">🌍 Language Translator</h1>', unsafe_allow_html=True)
st.markdown('<h3 class="subheader">Translate words or sentences easily in multiple languages</h3>', unsafe_allow_html=True)

# Split layout into two columns
col1, col2 = st.columns(2)

with col1:
    # User input for word/sentence
    word = st.text_input("Enter a word or sentence to translate:")

with col2:
    # Language search input
    search = st.text_input("Search for a language:")

    # Filter the languages based on the search term
    language_options = [language for language in LANGUAGES.values() if search.lower() in language.lower()]

    if not language_options:
        st.write("No languages match your search.")
    else:
        # Selectbox to choose the target language
        target_language = st.selectbox("Select the target language:", language_options)

# Translate button and display results
if word:
    # Detect the input language
    detected_language = translator.detect(word).lang
    detected_language_name = LANGUAGES[detected_language].capitalize()

    st.markdown(f"Detected Language: **{detected_language_name}**")

    # Add a button to trigger the translation
    if st.button("Translate"):
        # Get the code of the selected language
        target_language_code = list(LANGUAGES.keys())[list(LANGUAGES.values()).index(target_language)]
        translated = translator.translate(word, dest=target_language_code)

        # Display detected language and translated text
        st.markdown(f'<div class="result-box">Input Language: **{detected_language_name}**</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="result-box">Translated Text in {target_language}: **{translated.text}**</div>', unsafe_allow_html=True)

# Footer
st.markdown('<div class="footer">Powered by Google Translator API</div>', unsafe_allow_html=True)
