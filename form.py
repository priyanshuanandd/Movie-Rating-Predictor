# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 15:39:05 2024

@author: mepri
"""

import streamlit as st
import pandas as pd
from joblib import load

def rating_prediction():
    # Load your trained model 
    loaded_model = load('model.joblib')
    

    def movie_rating_prediction(Year, Duration, Votes, DirectorAvgRating, Actor1AvgRating, Actor2AvgRating, Actor3AvgRating):
        # Create a dictionary from inputs
        user_input = {
            'Year': [Year], 
            'Duration': [Duration], 
            'Votes': [Votes], 
            'DirectorAvgRating': [DirectorAvgRating],
            'Actor1AvgRating': [Actor1AvgRating],
            'Actor2AvgRating': [Actor2AvgRating],
            'Actor3AvgRating': [Actor3AvgRating]
        }

        # Convert dictionary to DataFrame
        input_df = pd.DataFrame(user_input)
        
        # Make prediction
        prediction = loaded_model.predict(input_df)
        
        # Display result and corresponding GIF
        st.success(f"The predicted movie rating is: {prediction[0]:.2f}")
        
        if prediction[0] > 6:
            st.image('https://gifdb.com/images/high/naruto-thumbs-up-eu5y408m5xvk84jx.webp')
        else:
            st.image('https://media.tenor.com/J7Jwf57vRfAAAAAi/anime.gif')


    def main():
        st.title('Movie Rating Prediction Form')
        st.image('https://64.media.tumblr.com/b22e7fe6dbddf2584fe0d59add5b9108/tumblr_ohank8ud6D1u9aqcno1_500.gifv', use_column_width=True)
        
        st.write("*The model is 96% accurate and takes into consideration the Year, Duration, Votes, and average ratings of the Director and Actors.")
        
        st.write("Enter the Movie Details: ")
        # Convert inputs to appropriate numerical types
        Year = st.number_input("Movie Release Year", min_value=1931, max_value=2021, step=1, format='%d')
        Duration = st.number_input("Movie Duration (in minutes)", min_value=21, step=1, format='%d')
        Votes = st.number_input("Number of Votes", min_value=5, step=1, format='%d')
        Director_Rating = st.number_input("Average Rating of Director", min_value=0.0, max_value=10.0, step=0.1, format='%f')
        Actor1_Rating = st.number_input("Average Rating of Actor 1", min_value=0.0, max_value=10.0, step=0.1, format='%f')
        Actor2_Rating = st.number_input("Average Rating of Actor 2", min_value=0.0, max_value=10.0, step=0.1, format='%f')
        Actor3_Rating = st.number_input("Average Rating of Actor 3", min_value=0.0, max_value=10.0, step=0.1, format='%f')
        
        if st.button('Predict Movie Rating'):
            movie_rating_prediction(int(Year), int(Duration), int(Votes), float(Director_Rating), float(Actor1_Rating), float(Actor2_Rating), float(Actor3_Rating))

    main()
