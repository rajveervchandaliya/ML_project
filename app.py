import streamlit as st

# Page title
st.title("Simple Streamlit Machine Learning App")

# Text input
user_text = st.text_input("Enter some text:")

# Display entered text
if user_text:
    st.write("You entered:")
    st.write(user_text)
else:
    st.write("Please enter some text above.")
