z# Indian IMDB Movie Rating Prediction

This project aims to predict movie ratings for Indian movies listed on IMDB. The dataset used is sourced from Kaggle and contains information such as movie name, year of release, genre, director, actors, duration, and rating.
## Dataset
Insights:
-Every column had null values except name column
=We also found that the following columns: Name, Year, Duration, Genre, and Votes had typos that were corrected later
-The null values in most of the columns were dropped and for Genre, it was filled with the mode value
-Later, we checked the duplicated values and dropped them based on Name column
## Technologies Used

**1. Python:** The entire project is implemented using Python, a versatile programming language widely used for data analysis, machine learning, and web development.

**2. Libraries:** Several Python libraries are employed to facilitate data manipulation, analysis, and modeling:

   - **Pandas:** Used for data cleaning, transformation, and analysis. It provides data structures like DataFrames for efficient data handling.
   - **NumPy:** Provides support for numerical operations, including array manipulation and mathematical functions.
   - **Seaborn and Matplotlib:** Used for data visualization, creating informative plots and charts to gain insights from the data.
   - **Scikit-learn:** A comprehensive machine learning library, used for model training, evaluation, and preprocessing tasks like scaling and imputation.
   - **Ydata-profiling:** Generates detailed data profiling reports, highlighting data quality issues, missing values, and descriptive statistics.
   - **LazyPredict:** Automates model selection and evaluation, comparing the performance of various machine learning algorithms.

**3. Jupyter Notebook:** An interactive development environment that allows for combining code, visualizations, and documentation in a single document.

**4. Kaggle:** A platform for hosting and sharing datasets, used to download the IMDB Indian movies dataset.

**5. Git and GitHub:** Version control system and online repository for managing and collaborating on code.

## Methodology

1. **Data Collection:** The dataset is downloaded from Kaggle.
2. **Data Cleaning and Preprocessing:** Missing values are handled using imputation techniques, and categorical variables are converted to numerical representations.
3. **Feature Engineering:** New features are created, such as average ratings for directors and actors, and a decade feature.
4. **Model Selection:** LazyRegressor is used to compare various regression models and identify the best-performing one.
5. **Model Training and Evaluation:** The selected model (Support Vector Regressor in this case) is trained on the training data and evaluated on the test data using metrics like Mean Squared Error and R-squared.
## Results
We get a R2 Score of 84 % from Support Vector Regressor
## Conclusion

In this Jupyter notebook project, we embarked on a journey to analyze and predict movie ratings. We encountered a variety of data challenges, such as missing values, typos in column names, and duplicated records. Through a series of data cleaning and preprocessing steps, we were able to prepare the dataset for analysis. Our analysis uncovered several interesting insights about the movie dataset. We observed trends in movie durations, genre popularity, the most prolific actors and directors, and the distribution of movie ratings and votes over the years. Notably, we found that short-duration movies tend to receive higher ratings and votes, and the Drama genre has consistently performed well in terms of ratings.



