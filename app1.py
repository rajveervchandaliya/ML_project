import streamlit as st

st.set_page_config(page_title="Text ML App")

st.header("My Machine Learning App")

text = st.text_input(
    "Type something below:",
    placeholder="Enter your text here..."
)

st.divider()

if text.strip():
    st.success("Your input was received!")
    st.write(f"**Entered text:** {text}")
else:
    st.info("Waiting for your input...")
