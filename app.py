#give me a simple streamlit app that can showcase the use of streamlit and the different components of streamlit
import streamlit as st

#print hello world in streamlit
st.write("Hello World")

#give me a button that says click me and when clicked it will print hello world in streamlit
button = st.button("Click me")
if button:
    st.write("Hello pillau maha lakka")

#give me a text input that says enter your name and when entered it will print hello name in streamlit
text_input = st.text_input("Enter your name")
if text_input:
    st.write(f"Hello {text_input}")

#give me a text area that says enter your message and when entered it will print hello message in streamlit
text_area = st.text_area("Enter your message")
if text_area:
    st.write(f"Hello {text_area}")

#give me a select box that says select your gender and when selected it will print hello gender in streamlit
select_box = st.selectbox("Select your gender", ["Male", "Female", "Other"])
if select_box:
    st.write(f"Hello {select_box}")

#give me a radio button that says select your gender and when selected it will print hello gender in streamlit
radio_button = st.radio("Select your gender", ["Male", "Female", "Other"])
if radio_button:
    st.write(f"Hello {radio_button}")

#give me a checkbox that says select your gender and when selected it will print hello gender in streamlit
checkbox = st.checkbox("Select your gender")
if checkbox:
    st.write(f"Hello {checkbox}")