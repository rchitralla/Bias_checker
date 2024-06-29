import streamlit as st
import subprocess
from transformers import pipeline

# Ensure the SpaCy model is downloaded
try:
    import spacy
    nlp = spacy.load("en_core_web_sm")
except:
    subprocess.run(["python", "-m", "spacy", "download", "en_core_web_sm"])
    import spacy
    nlp = spacy.load("en_core_web_sm")

# Load the transformer model
classifier = pipeline('text-classification', model='unitary/toxic-bert')

# Streamlit app layout
st.title("Text Bias Checker")
st.write("Enter text to check for bias against women:")

text_input = st.text_area("Text Input", height=200)

if st.button("Check Bias"):
    if text_input:
        results = classifier(text_input)
        if results:
            st.write("Bias Detected:")
            for result in results:
                st.markdown(f"**{result['label']}**: {result['score']:.2f}")
        else:
            st.write("No bias detected.")
    else:
        st.write("Please enter some text to analyze.")
