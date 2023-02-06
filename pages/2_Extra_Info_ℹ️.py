"""
This file contains the code to add my CV to the streamlit app.
"""
import streamlit as st


st.title("A Little More About Me...")

# Write about yourself.
st.write("""
At the height of the pandemic, I made a rather shocking discovery for a psychology undergraduate student - 
I was enjoying my statistics modules. This led me to tailor my degree to the pursuit of more 
quantitative and scientific fields of study. 
To supplement this, I taught myself python programming and more advanced maths. 
I used my dissertation to gain practical experience with these skills, and created a predictive model 
for the adoption intention of autonomous vehicles in Ireland.
""")
st.write("""
I am now studying for a 30 ECTS credit postgraduate certificate in Data Science at Technological University Dublin.
I supplement my learning by providing programming and statistics tutoring to 
undergrad students from a wide array of academic disciplines. I also recently started freelance data analytics, 
which has allowed me to work on many exciting real world projects that are having an impact. 
""")

# Write skills display
col1,col2 = st.columns(2)
with col1:
    st.header("Technical Skills ⚙️")
    st.button("Object Oriented Programming")
    st.button("Python")
    st.button("SQL")
    st.button("SPSS")
    st.button("Statistics")
    st.button("Data Visualisation - Streamlit, Plotly, Matplotlib")
    st.button("Data Wrangling - Numpy,Pandas")

with col2:
    st.header("Soft Skills 🗣️")
    st.button("Communication")
    st.button("Collaboration")
    st.button("Attention to Detail")
    st.button("Highly Organised")
    st.button("Administration")
    st.button("Spanish (B1.4)")