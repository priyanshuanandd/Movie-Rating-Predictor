# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 15:39:05 2024

@author: mepri
"""
import streamlit as st
import pandas as pd
from joblib import load
import os
# Print current working directory
print(os.getcwd())
def rating_prediction():
    
    
    # Specify the relative path to your model file
    model_path = 'model.joblib'
    
    # Load your trained model 
  #  loaded_model = load(model_path)
    
    def movie_rating_prediction(Year, Duration, Votes, Weighted_Rating, Decade):
        # Create a dictionary from inputs
        user_input = {
            'Year': [Year], 
            'Duration': [Duration], 
            'Votes': [Votes], 
            'Weighted_Rating': [Weighted_Rating],
            'Decade': [Decade]
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
        
        st.write("*The model is 96% accurate and takes into consideration the Year, Decade, Weighted Rating, Duration, and Votes.")

        st.write("Enter the Movie Details: ")
            
        # Convert inputs to appropriate numerical types
        Year = st.number_input("Movie Release Year", min_value=1931, max_value=2021, step=1, format='%d')
        Duration = st.number_input("Movie Duration (in minutes)", min_value=21, step=1, format='%d')
        Votes = st.number_input("Number of Votes", min_value=5, step=1, format='%d')
        Weighted_Rating = st.number_input("Weighted Rating", min_value=9.0, step=0.1, format='%f')
        Decade = (Year // 10) * 10
        
        if st.button('Predict Movie Rating'):
            movie_rating_prediction(int(Year), int(Duration), int(Votes), float(Weighted_Rating), int(Decade))

    main()
