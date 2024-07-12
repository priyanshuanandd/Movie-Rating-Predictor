import streamlit as st
from PIL import Image

def welcome():
    
    st.image('https://i.pinimg.com/originals/bc/31/d5/bc31d54d068f23d9d4f859ea6a276dad.gif',use_column_width=True)
    # Introduction
    st.title("Movie Rating Prediction App")
    st.write("Embark on a cinematic adventure as we predict movie ratings using machine learning. This web app leverages data insights to estimate a movie's rating based on various features.")

    # Key Features
    st.subheader("Key Features:")
    st.write('''1. **Predictive Analytics:**
    Explore the predictions of movie ratings using advanced analytics. The model considers features like release year, duration, director, and more.''')

    st.write('''2. **User-Friendly Interface:**
    Navigate through the app effortlessly. No expertise required – simply input movie details and discover the predicted rating.''')
    
    # About the Project
    st.subheader("About the Project:")
    st.write("The Movie Rating Prediction project blends the magic of movies with data science techniques. Join us in exploring the features that contribute to predicting a movie's rating.")

    # About You
    st.subheader("My Socials : ")
    st.write("[LinkedIn](https://linkedin.com/in/priyanshuanandd/)")

    # Call to Action
    st.write("Ready to explore the world of movie ratings? Head over to the **Data Overview** page to dive into the dataset and make your own rating predictions!")