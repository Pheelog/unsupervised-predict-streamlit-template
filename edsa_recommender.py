"""

    Streamlit webserver-based Recommender Engine.

    Author: Explore Data Science Academy.

    Note:
    ---------------------------------------------------------------------
    Please follow the instructions provided within the README.md file
    located within the root of this repository for guidance on how to use
    this script correctly.

    NB: !! Do not remove/modify the code delimited by dashes !!

    This application is intended to be partly marked in an automated manner.
    Altering delimited code may result in a mark of 0.
    ---------------------------------------------------------------------

    Description: This file is used to launch a minimal streamlit web
	application. You are expected to extend certain aspects of this script
    and its dependencies as part of your predict project.

	For further help with the Streamlit framework, see:

	https://docs.streamlit.io/en/latest/

"""
# Streamlit dependencies
import streamlit as st

# Data handling dependencies
import pandas as pd
import numpy as np

# Custom Libraries
from utils.data_loader import load_movie_titles
from recommenders.collaborative_based import collab_model
from recommenders.content_based import content_model

# Data Loading
title_list = load_movie_titles('resources/data/movies.csv')

# App declaration
def main():

    # DO NOT REMOVE the 'Recommender System' option below, however,
    # you are welcome to add more options to enrich your app.
    page_options = ["Recommender System","Solution Overview", "About Us"]

    # -------------------------------------------------------------------
    # ----------- !! THIS CODE MUST NOT BE ALTERED !! -------------------
    # -------------------------------------------------------------------
    page_selection = st.sidebar.selectbox("Choose Option", page_options)
    if page_selection == "Recommender System":
        # Header contents
        st.write('# Movie Recommender Engine')
        st.write('### EXPLORE Data Science Academy Unsupervised Predict')
        st.image('resources/imgs/Image_header.png',use_column_width=True)
        # Recommender System algorithm selection
        sys = st.radio("Select an algorithm",
                       ('Content Based Filtering',
                        'Collaborative Based Filtering'))

        # User-based preferences
        st.write('### Enter Your Three Favorite Movies')
        movie_1 = st.selectbox('Fisrt Option',title_list[14930:15200])
        movie_2 = st.selectbox('Second Option',title_list[25055:25255])
        movie_3 = st.selectbox('Third Option',title_list[21100:21200])
        fav_movies = [movie_1,movie_2,movie_3]

        # Perform top-10 movie recommendation generation
        if sys == 'Content Based Filtering':
            if st.button("Recommend"):
                try:
                    with st.spinner('Crunching the numbers...'):
                        top_recommendations = content_model(movie_list=fav_movies,
                                                            top_n=10)
                    st.title("We think you'll like:")
                    for i,j in enumerate(top_recommendations):
                        st.subheader(str(i+1)+'. '+j)
                except:
                    st.error("Oops! Looks like this algorithm does't work.\
                              We'll need to fix it!")


        if sys == 'Collaborative Based Filtering':
            if st.button("Recommend"):
                try:
                    with st.spinner('Crunching the numbers...'):
                        top_recommendations = collab_model(movie_list=fav_movies,
                                                           top_n=10)
                    st.title("We think you'll like:")
                    for i,j in enumerate(top_recommendations):
                        st.subheader(str(i+1)+'. '+j)
                except:
                    st.error("Oops! Looks like this algorithm does't work.\
                              We'll need to fix it!")


    # -------------------------------------------------------------------

    # ------------- SAFE FOR ALTERING/EXTENSION -------------------
    if page_selection == "Solution Overview":
        st.title("Problem statement")
        st.write("To build a robust Machine Learning Model that will be able to accurately give personalised movies reccommendations to movie lovers. Hence, generating platform affinity for the streaming services which best facilitates their audience's viewing.")
        
        st.image('resources/imgs/image1.png',use_column_width=True)
        
        st.title("EDA")
        st.write("Primarily, EDA is for seeing what the data can tell us beyond the formal modeling or hypothesis testing task.This approach for data analysis uses many tools(mainly graphical to maximize insight into a data set, extract important variables, detect outliers and anomalies, amongst other details that is missed when looking at DataFrame. This step is very important especially when we model the data in order to apply Machine Learning techniques.")
        
        st.image('resources/imgs/image2.png',use_column_width=True)
        st.write("This chart shows the top 30 most rated movies. Shawshank Redemption got the most rating. Some movies got an average of 5 stars rating, but in the course of our analysis, we discovered that the number of ratings they got was very few, hence that was possible. What this chart shows is that, Shawshank Redemption got the most number of Users rating it >3.9 .")
        
        st.image('resources/imgs/image3.png',use_column_width=True)
        st.write("This chart shows the top 30 movie viewers. This information is useful to identify the movie preference of top customers. these top customers are most likely influencers and can make users watch a movie they probably wouldn't have considered watching.")
        
        st.image('resources/imgs/image4.png',use_column_width=True)
        st.write("This chart shows the years with the highest number of movies produced. This information will help you to visually explore how the movie industry has performed over the years")
        
        st.image('resources/imgs/image5.png',use_column_width=True)
        st.write("This chart shows the genres that appears most in the dataset we trained our model with. This information will enable us understand the genres of movies produced most for the period the data was captured.")
        
    if page_selection == "About Us":
        st.image('resources/imgs/Originals_Logo.png',width=400)
        
        st.title("About Us")
        st.write("The source, the core from where every creativity and ingenuity emanates, \
                  The Originals, we are a team of data scientist, sold out to solving \
                  real human problems with flavour and style. ")
        
        st.image('resources/imgs/pheel.png',use_column_width=True)
        
        st.title("Our Mission")
        st.write("Use data to optimize human possibilities of attaining excellence, one solution at a time.")
        
        st.title("Our Vision")
        st.write("Improve living conditions, championing new innovations powered by data")
        


    # You may want to add more sections here for aspects such as an EDA,
    # or to provide your business pitch.


if __name__ == '__main__':
    main()
