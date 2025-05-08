import streamlit as st
from transformers import pipeline

# Title
st.title("English to Hindi Translator 🗣️📘➡️📙")

# Text input
user_input = st.text_area("Enter text in English", placeholder="e.g., This is very good food")

# Load the translation model
@st.cache_resource
def load_model():
    return pipeline(
        task="translation_en_to_hi",
        model="Helsinki-NLP/opus-mt-en-hi",
        device=0  # Use -1 for CPU if you don't have GPU
    )

translator = load_model()

# Button to translate
if st.button("Translate"):
    if user_input:
        translation = translator(user_input)[0]['translation_text']
        st.success("Translated Text (Hindi):")
        st.markdown(f"**{translation}**")
    else:
        st.warning("Please enter some text to translate.")

# Footer
st.markdown("---")
st.caption("Built with 🤗 Hugging Face and Streamlit")
