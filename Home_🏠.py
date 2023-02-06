"""
This main file contains the home page for the portfolio website.
"""
# Importing required modules/libraries
import streamlit as st
from streamlit_lottie import st_lottie
from read_animations import read_lottie


# Storing lottie files (used as the animations on the website)
maths_lottie = read_lottie("https://assets10.lottiefiles.com/packages/lf20_pan8jtpf.json")
coding_lottie = read_lottie("https://assets10.lottiefiles.com/packages/lf20_49rdyysj.json")
data_lottie = read_lottie("https://assets3.lottiefiles.com/packages/lf20_bdlrkrqv.json")

with st.container():
    # Make a title
    st.title("Ryan O'Connor - My Portfolio 👋")

    # Create two columns where my portrait and description will be stored.
    col1,col2 = st.columns(2)

    # Add portrait and description
    with col1:
        st.image("images/portrait.png",width=300)

    with col2:
        st.subheader('About me')
        content = """
        Hello! My name is Ryan O'Connor. I am a postgraduate student in Data Science at Technological University Dublin.
        I have coded this website to showcase my skills in Data Science and Analytics. Some of my sample projects are
        listed below.
        """
        st.write(content)
        st.write("")
        st.subheader('What I do')
        st.write("""
        I specialise in offering data analytics and data cleaning services to small businesses, 
        research teams and students. For more info, drop me an email at ryan19.roc@gmail.com. 
        """)

# Add the quantitative skills section
with st.container():
    st.write('---')
    st.write(" ")
    st.header("Quantitative Skills 🧮")
    st.write("""
    Here are some projects that highlight my quantitative abilities and skills in working with complex data. 
    """)
    col1,col2 = st.columns(2)
    with col1:
        # Statistics
        st.subheader("Statistics")
        st.write("""
                A sample of my statistics capabilities. This is my group project from Utrecht University's 
                summer program in data science. [Source Code](https://github.com/ryanoc21/UU_Data_Science_Project) 
                """)

        # Linear Algebra
        st.subheader("Linear Algebra")
        st.write("""
        A sample of code challenges that cover a wide array of relevant topics. 
        They include Eigendecomposition, Applications of Orthogonalization in the 
        Least Squared Algorithm, and Singular Value Decomposition. 
        [Source Code](https://github.com/ryanoc21/Linear-Algebra) 
        """)

        # Calculus
        st.subheader("Calculus")
        st.write("""
        A sample of coding challenges covering a range of relevant topics in calculus. 
        [Source Code](https://github.com/ryanoc21/Calculus-Code).
        """)

    with col2:
        st_lottie(maths_lottie,height=500,key='maths')

# Analytic/Programming Skills
with st.container():
    st.write('---')
    st.write(" ")
    st.header("Data Analysis 📊 and Programming 💻")
    st.write("""
    Here are some of my projects that highlight my abilities in data analysis and programming. 
    """)
    col1,col2 = st.columns(2)
    with col1:
        # Weather App
        st.subheader("Weather Forecasting App ☀️")
        st.write("""
        A streamlit web app that takes weather data from the open weather API. The user can input their 
        chosen weather type for the next 5 days in their chosen city and the app will display the weather to them.
        [View the App](https://ryanoc21-revised-weather-forecast-web-app-main-ryp7aq.streamlit.app)
        """)

        # Football App
        st.subheader("Premier League Top Scorers App ⚽️")
        st.write("""
        A streamlit web app that scrapes premier league top scorer data from a popular football stats website. 
        The user can choose which team they want to view the data for and the relevant bar chart will be displayed. 
        [View the App](https://ryanoc21-pl-statistics-streamlit-app-main-jvg010.streamlit.app)
        """)

        # Economic Data App
        st.subheader("Irish Economic Data App 💶")
        st.write("""
        This app takes Irish economic data concerning property prices, unemployment rates and inflation from the 
        Fred API. The user can choose which type of data they want to plot and an interactive time series graph 
        will be displayed. [View the App](https://ryanoc21-fred-economic-api-main-5x16sb.streamlit.app)
        """)

        # Database
        st.subheader("Sample Airport Database Design (SQL) ✈️")
        st.write("""
        This is the code for my final information systems assignment @ TU Dublin. 
        It covers a conceptual design for a relational database for an airport. 
        A full process of normalisation was also carried out. 
        Finally, fake data were created to implement the database in MySQL.
        A wide array of SQL queries were carried out, along with the creation of various indexes and a dump file.
        I received 98% for this project. [Source Code](https://github.com/ryanoc21/RDBMS-Design-and-SQL-) 
        """)

    with col2:
        st_lottie(coding_lottie,height=500,key='coding')
        st_lottie(data_lottie,height=400,key='data')