import streamlit as st
import spacy

# Load the SpaCy model
nlp = spacy.load("en_core_web_sm")

# Define bias terms (you can expand this list)
bias_terms = ["bossy", "hysterical", "emotional", "shrill", "nagging"]

# Function to check bias in text
def check_bias(text):
    doc = nlp(text)
    results = []

    for token in doc:
        if token.lower_ in bias_terms:
            results.append({
                'text': token.text,
                'start': token.idx,
                'end': token.idx + len(token),
                'label': 'BIAS'
            })

    return results

# Streamlit app layout
st.title("Text Bias Checker")
st.write("Enter text to check for bias against women:")

text_input = st.text_area("Text Input", height=200)

if st.button("Check Bias"):
    if text_input:
        results = check_bias(text_input)
        if results:
            st.write("Bias Detected:")
            for result in results:
                st.markdown(f"**{result['text']}** (Position: {result['start']}-{result['end']})")
        else:
            st.write("No bias detected.")
    else:
        st.write("Please enter some text to analyze.")
