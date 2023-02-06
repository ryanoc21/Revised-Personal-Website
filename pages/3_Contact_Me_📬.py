"""
This file contains the code for the contact me portion of my personal website.
"""
import streamlit as st


st.title("Get in touch")

with st.container():
    col1, col2, col3 = st.columns(3)

    with col1:
        st.image('images/linkedin.png')
        st.write("[Linkedin](https://www.linkedin.com/in/ryan-o’connor-0679821bb/)")

    with col2:
        st.image('images/github.png', width=190)
        st.write("[Github](https://github.com/ryanoc21)")

    with col3:
        st.image('images/gmail.png', width=190)
        st.write("ryan19.roc@gmail.com")

    st.write("---")